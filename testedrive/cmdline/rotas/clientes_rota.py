from testedrive.cmdline.telas.clientes_tela import tela_menu_clientes
from testedrive.controladores.cliente_ctrl import cadastrar_cliente
# Rotas
# nissan.com/testedrive/clientes/cadastrar-cliente
# nissan.com/testedrive/clientes/listar-cliente

def rota_clientes():
    while True:
        opcao = tela_menu_clientes()
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            # listar_clientes()
            print("2 escolhido")
        elif opcao == "0":
            break
        else:
            print("\n⚠️ Opção inválida.")