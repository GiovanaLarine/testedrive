from testedrive.db import Model
from sqlalchemy import Enum as SQLEnum, Integer, String, Text
from sqlalchemy.orm import mapped_column, relationship

from testedrive.modelos.enums import TipoRota


class Rota(Model):
    __tablename__ = "rotas"

    id = mapped_column(Integer, primary_key=True)
    nome = mapped_column(String(50), nullable=False)
    descricao = mapped_column(Text, nullable=True)
    tipo = mapped_column(SQLEnum(TipoRota, name="tipo_rota_enum"), nullable=False)

    veiculos = relationship("RotaVeiculo", back_populates="rota")