from datetime import datetime

class AgendaServico:
    def __init__(self, datas_indisponiveis, dias_semana_indisponiveis,horario_padrao, duracao_agendamento,):
         self.datas_indisponiveis = datas_indisponiveis
         self.dias_semana_indisponiveis = dias_semana_indisponiveis
         self.horario_padrao = horario_padrao
         self.duracao_agendamento = duracao_agendamento
         self.horarios_especiais=None

    def validar_data_horario(self, data_horario):
        return (
            self._data_futura(data_horario)
            and self._data_disponivel(data_horario)
            and self._dia_semana_disponivel(data_horario)
            and self._horario_funcionamento(data_horario)
        )

    def _data_futura(self, data_horario):
        return data_horario > datetime.now()
    
    def _data_disponivel(self, data_horario):
            return data_horario.date() not in self.datas_indisponiveis
    
    def _dia_semana_disponivel(self, data_horario):
        return data_horario.weekday() not in self.dias_semana_indisponiveis
    
    def _horario_funcionamento(self, data_horario):
        dia_semana = data_horario.weekday()
        horario_abertura, horario_fechamento = self.horarios_especiais.get(
            dia_semana, self.horario_padrao
        )
        horario = data_horario.time()
        limite = (
            datetime.combine(datetime.today(), horario_fechamento)
            - self.duracao_agendamento
        ).time()
        return horario_abertura <= horario <= limite