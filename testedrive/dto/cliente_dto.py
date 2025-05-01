from dataclasses import dataclass


@dataclass
class ClienteDTO:
    nome: str
    sobrenome: str
    email: str
    cpf: str
