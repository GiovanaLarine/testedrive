from testedrive.db import Model
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
""" 
    sqlalchemy uma biblioteca ORM (Object Relational Mapper) 

    ORM liga uma tabela do banco a uma classe do python

"""

class Cliente(Model):
    __tablename__ = "clientes"

    id = mapped_column(Integer, primary_key=True)
    nome = mapped_column(String(50), nullable=False)
    sobrenome = mapped_column(String(70), nullable=False)
    email = mapped_column(String(100), nullable=False)
    cpf = mapped_column(String(11), unique=True, nullable=False)