from agendamentos import verificar_data_valida
from datetime import datetime

def main():
    print("=== Sistema de Agendamento de Test Drive ===\n")
    data = input("Escolha uma data (DD/MM/AAAA): ")
    horario = input("Escolha um horario (HH:MM)")
    data_horario = f"{data} {horario}"
    # datetime.strptime(data_horario, '%d/%m/%Y %H:%M')
    valido = verificar_data_valida(data_horario)

    if valido:
        print("Horario valido!")
    else:
        print("horario invalido!")

if __name__ == "__main__":
    main()