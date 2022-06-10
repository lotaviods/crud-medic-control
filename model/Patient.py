class Patient():
    cpf: str
    name: str
    email: str
    phoneNumber: str

    def __init__(self, cpf: str, name: str, email: str, phoneNumber: str) -> None:
        self.cpf = cpf
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        pass

    def __str__(self) -> str:
        return f"{self.name} | cpf: {self.cpf} | email: {self.email} | celular: {self.phoneNumber}"