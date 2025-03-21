from datetime import datetime, timedelta

class Agendamento:
    def __init__(
        self,
        id: str,
        cliente_id: str,
        veiculo_id: int,
        data_horario: datetime,
        duracao: timedelta,
    ):
        self.id = id
        self.cliente_id = cliente_id
        self.veiculo_id = veiculo_id
        self.data_horario = data_horario
        self.duracao = duracao
        self.status = "agendado"

    def intervalo(self):
        return self.data_horario, self.data_horario + self.duracao

    def cancelar(self):
        self.status = "cancelado"