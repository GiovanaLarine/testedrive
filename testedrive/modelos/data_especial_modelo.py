from testedrive.db import Model
from sqlalchemy import Date, Integer, Time, Text
from sqlalchemy.orm import mapped_column


class DataEspecial(Model):
    __tablename__ = "datas_especiais"

    id = mapped_column(Integer, primary_key=True)
    data = mapped_column(Date, unique=True, nullable=False)
    abre = mapped_column(Time, nullable=True)
    fecha = mapped_column(Time, nullable=True)
    motivo = mapped_column(Text, nullable=True)