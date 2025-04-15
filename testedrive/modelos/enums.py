from enum import Enum

class TipoUsuario(Enum):
    VENDEDOR = "vendedor"
    GERENTE = "gerente"

class StatusAgendamento(Enum):
    AGENDADO = "agendado"
    EM_ANDAMENTO = "em_andamento"
    FINALIZADO = "finalizado"
    CANCELADO = "cancelado"

class TipoRota(Enum):
    URBANA = "urbana"
    RURAL = "rural"
    OFFROAD = "offroad"


