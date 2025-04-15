from testedrive.db import Model
from sqlalchemy import DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import mapped_column


class Manutencao(Model):
    __tablename__ = "manutencoes"

    id = mapped_column(Integer, primary_key=True)
    veiculo_id = mapped_column(Integer, ForeignKey("veiculos.id"), nullable=False)
    data_hora_inicio = mapped_column(DateTime, nullable=False)
    data_hora_fim = mapped_column(DateTime, nullable=False)
    descricao = mapped_column(Text, nullable=True)
