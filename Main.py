import sqlite3
from typing import List
from model.History import History
from model.Patient import Patient
from util.Menu import Menu
from model.MenuOption import DELETE_HISTORY, DELETE_PATIENT, LIST_PATIENTS, REGISTER_HISTORY, REGISTER_PATIENT, SEARCH_PATIENT_CPF, UPDATE_PATIENT, MenuOption, MenuSelection
from util.SqlHelper import SqlHelper
from util.UserInputHelper import UserInputHelper
from util.exceptions.PatientNotFound import PatientNotFound
from util.exceptions.PatientWithHistory import PatientWithHistory


class Main():
    connection = sqlite3.connect("trab.db")
    sqlHelper = SqlHelper(connection)

    def main(self):
        self.sqlHelper.createTablesIfNeeded()

        while True:
            Menu.faixa("Controle Médico")

            menuOption: MenuOption = Menu.menu()

            if(menuOption.menuSelection == MenuSelection.HISTORY):
                if(menuOption.option == REGISTER_HISTORY):
                    Menu.faixa("Registro de histórico")

                    history = UserInputHelper.generateHistoryByUserInput()

                    self.__registerHistory(history)

                if(menuOption.option == DELETE_HISTORY):
                    Menu.faixa("Deletar histórico")
                    self.__getHistoriesByCpf()

                    self.__deleteHistory()

            elif(menuOption.menuSelection == MenuSelection.PATIENT):

                if(menuOption.option == REGISTER_PATIENT):
                    Menu.faixa("Registro de paciente")
                    self.__registerPatient()
                elif (menuOption.option == LIST_PATIENTS):
                    Menu.faixa("Lista de pacientes")

                    self.__listPatient()
                elif (menuOption.option == SEARCH_PATIENT_CPF):
                    Menu.faixa("Busca de paciente")
                    self.__searchPatient()
                elif (menuOption.option == DELETE_PATIENT):
                    Menu.faixa("Exclusão de paciente")
                    self.__deletePatient()
                elif (menuOption.option == UPDATE_PATIENT):
                    Menu.faixa("Atualização de paciente")
                    self.__updatePatient()

    def __registerPatient(self):
        patient = UserInputHelper.generatePatientByUserInput()

        try:
            result = self.sqlHelper.insertPatient(patient)
            if(result):
                print("\nPaciente cadastrado com sucesso!\n")
        except:
            print("\nPaciente já existente, não foi possível adiciona-lo\n")

    def __registerHistory(self, history: History):
        try:
            result = self.sqlHelper.insertHistory(history)
            if(result):
                print("\nHistórico cadastrado com sucesso!\n")
        except PatientNotFound:
            print("\nPaciente é inválido\n")

    def __getHistoriesByCpf(self):
        try:
            cpf = str(input("\nDigite o cpf do paciente: "))

            result: List[History] = self.sqlHelper.queryHistoriesByCpf(cpf)

            for histories in result:
                print(histories)

        except PatientNotFound:
            print("\Historico não encontrado\n")

    def __deleteHistory(self):
        code = str(input("\nDigite o código do histórico: "))

        result = self.sqlHelper.deleteHistory(code)

        if(result):
            print("\nHistórico excluido com sucesso!\n")
        else:
            print("\nHistórico não encontrado!")

    def __listPatient(self):
        try:
            results: List[Patient] = self.sqlHelper.queryPatients()

            if(len(results) == 0):
                print("Nenhum paciente cadastrado!\n")
            else:
                for patient in results:
                    print(f"{patient}")
                print("\n")
        except:
            print("\nOcorreu erro ao buscar pacientes\n")

    def __searchPatient(self):
        try:
            cpf = str(input("\nDigite o cpf do paciente: "))
            result: Patient = self.sqlHelper.queryPatientByCpf(cpf)
            print(f"Paciente: {result.name}")
        except PatientNotFound:
            print(f"Paciente não encontrado")

    def __deletePatient(self):
        try:
            cpf = str(input("\nDigite o cpf do paciente: "))
            result = self.sqlHelper.deletePatientByCpf(cpf)

            if(result):
                print(f"\nPaciente excluido com sucesso!\n")
            else:
                print("\nPaciente não encontrado\n")

        except PatientWithHistory:
            print(f"\nPaciente contém historico cadastrado!\nNão foi possível excluir\n")

    def __updatePatient(self):
        cpf = str(input("\nDigite o cpf do paciente: "))

        newEmail = str(input("Digite o novo email: "))
        newNumber = str(input("Digite o novo numero do paciente: "))

        result = self.sqlHelper.updatePatient(cpf, newEmail, newNumber)

        if(result):
            print(f"Paciente atualizado com sucesso!\n")
        else:
            print("\nPaciente não cadastrado\n")


if __name__ == '__main__':
    Main().main()
