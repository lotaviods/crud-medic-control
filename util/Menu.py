from model.MenuOption import *


class Menu:
    @staticmethod
    def menu():
        try:
            option = int(input('\n1. Menu paciente'
                               '\n2. Menu historico'
                               '\n3. Sair'
                               '\n\nOpção >> '))
            if(option == 1):
                option = int(input(f'\n{REGISTER_PATIENT}. Cadastrar paciente'
                                   f'\n{LIST_PATIENTS}. Listar pacientes'
                                   f'\n{UPDATE_PATIENT}. Alterar paciente'
                                   f'\n{DELETE_PATIENT}. Excluir paciente'
                                   f'\n{SEARCH_PATIENT_CPF}. Consultar paciente por cpf'
                                   '\n'
                                   '\n\nOpção >> '))

                return MenuOption(selection=MenuSelection.PATIENT, option=option)

            elif(option == 2):
                option = int(input(f'\n{REGISTER_HISTORY}. Cadastrar historico'
                                   f'\n{SEARCH_HISTORY}. Consultar historico'
                                   f'\n{DELETE_HISTORY}. Excluir historico'
                                   '\n'
                                   '\n\nOpção >> '))

                return MenuOption(selection=MenuSelection.HISTORY, option=option)
            elif (option == 3):
                exit()
            else:
                print("\nOpção invalida")
                return MenuOption(selection=MenuSelection.NONE, option=0)
        except (ValueError):
            print("\nOpção invalida")
            return MenuOption(selection=MenuSelection.NONE, option=0)

    @staticmethod
    def faixa(texto):
        print('-' * 40)
        print(texto.upper().center(40))
        print('-' * 40)
