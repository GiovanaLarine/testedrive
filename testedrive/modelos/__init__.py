from .agendamento_modelo import Agendamento
from .cliente_modelo import Cliente
from .data_especial_modelo import DataEspecial
from .horario_funcionamento_modelo import HorarioFuncionamento
from .manutencao_modelo import Manutencao
from .reserva_modelo import Reserva
from .rota_modelo import Rota
from .rota_veiculo_modelo import RotaVeiculo
from .usuario_modelo import Usuario
from .veiculo_modelo import Veiculo
from .vendedor_modelo import Vendedor
from testedrive.db import Model, engine


def registrar_modelos():
    Model.metadata.create_all(engine)


__all__ = [
    "registrar_modelos",
    "Agendamento",
    "Cliente",
    "DataEspecial",
    "HorarioFuncionamento",
    "Manutencao",
    "Reserva",
    "Rota",
    "RotaVeiculo",
    "Usuario",
    "Veiculo",
    "Vendedor",
]
