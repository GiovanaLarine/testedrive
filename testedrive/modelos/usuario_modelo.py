from testdrive.db import Model
from sqlalchemy import Integer, String, Enum as SQLEnum
from sqlalchemy.orm import mapped_column, relationship

from testedrive.modelos.enums import TipoUsuario

class Usuario(Model):
    __tablename__ = "usuarios"

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String(100), unique=True, nullable=False)
    senha = mapped_column(String(128), nullable=False)
    tipo = mapped_column(SQLEnum(TipoUsuario, name="tipo_usuario_enum"), nullable=False)

    vendedor = relationship("Vendedor", back_populates="usuario", uselist=False)