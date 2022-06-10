class History:
    code: str = 0
    date: str
    patientCpf: str
    description: str
    finishedProcedures: str
    recommendedTreatments: str

    def __init__(self, code: int, date: str, patientCpf: str, description: str, finishedProcedures: str, recommendedTreatments: str) -> None:
        self.code = code
        self.date = date
        self.patientCpf = patientCpf
        self.description = description
        self.finishedProcedures = finishedProcedures
        self.recommendedTreatments = recommendedTreatments
        pass

    def __str__(self) -> str:
        return f"Codigo: {self.code} | data: {self.date} | descrição: {self.description} | Procedimentos realizados: {self.finishedProcedures} | Tratamentos recomendados: {self.recommendedTreatments}"
