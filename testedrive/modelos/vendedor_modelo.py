from testedrive.db import Model
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship


class Vendedor(Model):
    __tablename__ = "vendedores"

    id = mapped_column(Integer, primary_key=True)
    nome = mapped_column(String(50), nullable=False)
    sobrenome = mapped_column(String(70), nullable=False)
    avatar_url = mapped_column(String(255), nullable=True)  # URL com tamanho generoso
    usuario_id = mapped_column(
        Integer, ForeignKey("usuarios.id"), unique=True, nullable=False
    )

    usuario = relationship("Usuario", back_populates="vendedor")