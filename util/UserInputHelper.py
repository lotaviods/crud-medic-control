from model.History import History
from model.Patient import Patient


class UserInputHelper():
    
    @staticmethod
    def generatePatientByUserInput() -> Patient:
        name = str(input("\ndigite o nome do paciente: "))
        cpf = str(input("\ndigite o cpf do paciente: "))
        email = str(input("\ndigite o e-mail do paciente: "))
        phoneNumber = str(input("\ndigite o numero de celular do paciente: "))

        return Patient(cpf, name, email, phoneNumber)
    
    @staticmethod
    def generateHistoryByUserInput() -> History:
        date = str(input("Digite a data do histórico: "))
        patientCpf = str(input("Digite o cpf do paciente: "))
        description = str(input("Digite a descricao do histórico: "))
        finishedProcedures = str(input("Digite os procedimentos finalizados: "))
        recommendedTreatments = str(input("Digite os tratamentos recomendados: "))
        
        return History(0, date, patientCpf, description, finishedProcedures, recommendedTreatments)