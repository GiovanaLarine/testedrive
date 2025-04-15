from testedrive.db import Model
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import mapped_column, relationship


class RotaVeiculo(Model):
    __tablename__ = "rota_veiculo"

    id = mapped_column(Integer, primary_key=True)
    rota_id = mapped_column(Integer, ForeignKey("rotas.id"))
    veiculo_id = mapped_column(Integer, ForeignKey("veiculos.id"))

    rota = relationship("Rota", back_populates="veiculos")
    veiculo = relationship("Veiculo", back_populates="rotas")