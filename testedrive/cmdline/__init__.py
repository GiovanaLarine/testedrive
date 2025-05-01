from testedrive.cmdline.rotas import rota_clientes
from testedrive.cmdline.telas.menu_principal_tela import tela_menu_principal


def cli():
    while True:
        opcao = tela_menu_principal()
        if opcao == "1":
            # rota_agendamentos()
            pass
        elif opcao == "2":
            rota_clientes()
        elif opcao == "3":
            # rota_veiculos()
            pass
        elif opcao == "4":
            # rota_rotas()
            pass
        elif opcao == "0":
            print("\n👋 Encerrando o sistema.")
            break
        else:
            print("\n⚠️ Opção inválida.")
