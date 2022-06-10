from __future__ import annotations
import sqlite3
from typing import List
from model.History import History
from model.Patient import Patient
from util.exceptions.NoHistoryFound import NoHistoryFound
from util.exceptions.PatientNotFound import PatientNotFound
from util.exceptions.PatientWithHistory import PatientWithHistory


class SqlHelper:
    connection: sqlite3.Connection

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection
        pass

    def __createPatientTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            'CREATE TABLE patient(cpf TEXT PRIMARY KEY, name TEXT, email TEXT, phone_number TEXT)')
        cursor.close()

    def __createHistoryTable(self):
        cursor = self.connection.cursor()
        cursor.execute(
            'CREATE TABLE history(code INTEGER PRIMARY KEY AUTOINCREMENT, patient_cpf TEXT, date TEXT, description TEXT, finished_procedures TEXT, recommended_treatments TEXT, FOREIGN KEY(patient_cpf) REFERENCES patient(cpf))')
        cursor.close()

    def createTablesIfNeeded(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='patient';")

        if cursor.fetchone() is None:
            self.__createPatientTable()

        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='history';")

        if cursor.fetchone() is None:
            self.__createHistoryTable()
        self.connection.commit()
        cursor.close()

    def insertPatient(self, patient: Patient) -> bool:
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO patient(cpf, name, email, phone_number) VALUES(?, ?, ?, ?)", (
            patient.cpf, patient.name, patient.email, patient.phoneNumber))
        self.connection.commit()
        rowCount = cursor.rowcount

        self.connection.commit()
        cursor.close()

        return True if rowCount == 1 else False

    def insertHistory(self, history: History) -> bool:
        cursor = self.connection.cursor()
        self.queryPatientByCpf(history.patientCpf)

        cursor.execute("INSERT INTO history(patient_cpf, date, description, finished_procedures, recommended_treatments) VALUES(?, ?, ?, ?, ?)", (
            history.patientCpf, history.date, history.description, history.finishedProcedures, history.recommendedTreatments
        ))
        self.connection.commit()
        rowCount = cursor.rowcount

        cursor.close()

        return True if rowCount == 1 else False

    def deleteHistory(self, code: int) -> bool:
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM history WHERE code=?", (code, ))
        self.connection.commit()
        rowCount = cursor.rowcount

        self.connection.commit()
        cursor.close()

        return True if rowCount == 1 else False

    def queryPatientByCpf(self, cpf: str) -> Patient | None:
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM patient WHERE cpf=?", (cpf,))

        row = cursor.fetchone()
        self.connection.commit()    

        cursor.close()
        if(row == None):
            raise PatientNotFound()

        return Patient(*row)

    def queryHistoriesByCpf(self, cpf: int):
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT * FROM history INNER JOIN patient ON patient_cpf = patient.cpf WHERE cpf = ?", (cpf,))
        row = cursor.fetchall()

        if(row == None):
            cursor.close()
            raise NoHistoryFound()

        hitories = []

        for item in row:
            hitories.append(History(code=item[0], date=item[2], patientCpf=item[1], description=item[3],
                            finishedProcedures=item[4], recommendedTreatments=item[5]))

        return hitories

    def deletePatientByCpf(self, cpf: str) -> Patient | None:
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT * FROM patient INNER JOIN history ON patient.cpf = history.patient_cpf WHERE cpf = ?", (cpf,))

        row = cursor.fetchone()

        if(row != None):
            cursor.close()
            raise PatientWithHistory()

        cursor.execute("DELETE FROM patient WHERE cpf = ?", (cpf,))
        self.connection.commit()
        cursor.close()

        return True if cursor.rowcount == 1 else False

    def queryPatients(self) -> List[Patient]:
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM patient")

        rows = cursor.fetchall()
        
        cursor.close()

        return [Patient(*row) for row in rows]

    def updatePatient(self, cpf: int, newEmail: str, newPhoneNumber: str):
        cursor = self.connection.cursor()

        cursor.execute(
            "UPDATE patient SET email = ?, phone_number = ? WHERE cpf = ?", (newEmail, newPhoneNumber, cpf))

        self.connection.commit()
        cursor.close()

        return True if cursor.rowcount == 1 else False


# Alteração. Peça o CPF, faça a busca na tabela,
# permitindo alterar apenas o e-mail e/ou telefone. Emita
# a mensagem de “Não cadastrado” caso não encontre.