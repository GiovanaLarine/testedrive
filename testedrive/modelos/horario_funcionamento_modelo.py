from sqlalchemy import Integer, Time
from testedrive.db import Model
from sqlalchemy.orm import mapped_column

class HorarioFuncionamento(Model):
    __tablename__ = "horarios_funcionamento"

    id = mapped_column(Integer, primary_key=True)
    dia_semana = mapped_column(Integer, nullable=False)  # 0 = domingo
    abre = mapped_column(Time, nullable=True)
    fecha = mapped_column(Time, nullable=True)