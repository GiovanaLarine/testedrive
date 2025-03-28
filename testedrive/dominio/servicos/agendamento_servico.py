import uuid
from testedrive.dominio.entidades.agendamento import Agendamento

class AgendamentoServico:
    def __init__(self, agendamento_repo, veiculo_repo, agenda_servico):
        self.agendamento_repo = agendamento_repo
        self.veiculo_repo = veiculo_repo
        self.agenda_servico = agenda_servico
    
    def criar_agendamento(self, cliente_id, veiculo_id, data_horario):
        # 1. Valida regras de funcionamento
        if not self.agenda_servico.validar_data_horario(data_horario):
            raise Exception(
                "Data ou horário inválido conforme a agenda de funcionamento."
            )

        # 2. Valida disponibilidade do veículo
        veiculo = self.veiculo_repo.buscar_por_id(veiculo_id)
        if not veiculo.disponivel:
            raise Exception("Veículo indisponível.")

        # 3. Valida se já existe agendamento conflitante
        if not self.verificar_disponibilidade(cliente_id, veiculo_id, data_horario):
            raise Exception("Horário já ocupado para este cliente ou veículo.")

        # 4. Cria agendamento
        novo_agendamento = Agendamento(
            id=str(uuid.uuid4()),
            cliente_id=cliente_id,
            veiculo_id=veiculo_id,
            data_horario=data_horario,
            duracao=self.agenda_servico.duracao_agendamento,
        )

        # 5. Salva no repositório
        self.agendamento_repo.salvar(novo_agendamento)

        return novo_agendamento

    def cancelar_agendamento(self, agendamento_id):
        # 1. puxar o agendamento
        agendamento = self.agendamento_repo.buscar_por_id(agendamento_id)
        
        # 2. verifica se existe
        if not agendamento:
            raise Exception("Agendamento não encontrado.")
        
        agendamento.cancelar()

        self.agendamento_repo.atualizar(agendamento)

        return agendamento
        
    def verificar_disponibilidade(
        self,
        cliente_id: str,
        veiculo_id: int,
        data_horario: datetime,
        ignore_id: str | None = None,
    ) -> bool:
        """Verifica se o cliente ou veículo já possuem agendamento no horário."""

        agendamentos_do_dia = self.agendamento_repo.buscar_por_data(data_horario.date())

        novo_inicio = data_horario
        novo_fim = data_horario + self.agenda_servico.duracao_agendamento

        for agendamento in agendamentos_do_dia:
            # Se for o próprio agendamento (em caso de edição), ignora
            if ignore_id and agendamento.id == ignore_id:
                continue

            agendamento_inicio, agendamento_fim = agendamento.intervalo()

            # Verifica conflito de cliente
            if agendamento.cliente_id == cliente_id:
                if novo_inicio < agendamento_fim and novo_fim > agendamento_inicio:
                    return False

            # Verifica conflito de veículo
            if agendamento.veiculo_id == veiculo_id:
                if novo_inicio < agendamento_fim and novo_fim > agendamento_inicio:
                    return False

        return True

