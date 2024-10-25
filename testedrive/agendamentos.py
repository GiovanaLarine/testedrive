from datetime import datetime

# limite simultaneo = 4
modelos_disponiveis = ["Nissan Kicks", "Nissan Sentra", "Nissan Frontier", "Nissan Versa"]

# verificar_data_valida
def verificar_data_valida(data_horario):

    data_horario_dt = datetime.strptime(data_horario, '%d/%m/%Y %H:%M')
    agora = datetime.now()

    # Verifica se a data é futura
    if data_horario_dt < agora:
        print("A data e horário devem ser futuros.")
        return False


    # Verifica se é domingo (0 = segunda-feira, 6 = domingo)
    dia_da_semana = data_horario_dt.weekday()
    if dia_da_semana == 6:
        print("Agendamentos não são permitidos aos domingos.")
        return False

    # Verifica o horário de funcionamento
    horario = data_horario_dt.time()
    horario_abertura = datetime.strptime('08:00', '%H:%M').time()
    horario_fechamento = datetime.strptime('17:00', '%H:%M').time()
    horario_fechamento_sabado = datetime.strptime('11:00', '%H:%M').time()

    # verificar se é Sábado
    if dia_da_semana == 5:
        if horario < horario_abertura or horario > horario_fechamento_sabado:
            print(f"Aos sábados, o horário de funcionamento é das {horario_abertura.strftime('%H:%M')} às {horario_fechamento_sabado.strftime('%H:%M')}.")
            return False
    else:  # Segunda a sexta
        if horario < horario_abertura or horario_fechamento:
            print(f"O horário de funcionamento é das {horario_abertura.strftime('%H:%M')} às {horario_fechamento.strftime('%H:%M')}.")
            return False
        
    return True


# verificar_disponibilidade

    # Verifica se o cliente já tem um agendamento nesse horário

    # Verifica se o modelo escolhido já foi agendado nesse horário


# agendar_test_drive

