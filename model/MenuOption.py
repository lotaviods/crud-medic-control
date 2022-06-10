from enum import Enum

REGISTER_PATIENT = 1
LIST_PATIENTS = 2
UPDATE_PATIENT = 3
DELETE_PATIENT = 4
SEARCH_PATIENT_CPF = 5
REGISTER_HISTORY = 1
SEARCH_HISTORY = 2
DELETE_HISTORY = 3

class MenuSelection(Enum):
    HISTORY = 1
    PATIENT = 2
    NONE = 0

class MenuOption:
    option: int
    menuSelection: MenuSelection

    def __init__(self, selection: MenuSelection, option: int) -> None:
        self.menuSelection = selection
        self.option = option

