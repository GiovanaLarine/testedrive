from testedrive.db import Model
from sqlalchemy import DateTime, ForeignKey, Enum as SQLEnum, Integer
from sqlalchemy.orm import mapped_column

from testedrive.modelos.enums import StatusAgendamento


class Agendamento(Model):
    __tablename__ = "agendamentos"

    id = mapped_column(Integer, primary_key=True)
    vendedor_id = mapped_column(Integer, ForeignKey("vendedores.id"), nullable=False)
    cliente_id = mapped_column(Integer, ForeignKey("clientes.id"), nullable=False)
    veiculo_id = mapped_column(Integer, ForeignKey("veiculos.id"), nullable=False)
    rota_id = mapped_column(Integer, ForeignKey("rotas.id"), nullable=False)
    data_hora_inicio = mapped_column(DateTime, nullable=False)
    data_hora_fim = mapped_column(DateTime, nullable=False)
    status = mapped_column(
        SQLEnum(StatusAgendamento, name="status_agendamento_enum"), nullable=False
    )