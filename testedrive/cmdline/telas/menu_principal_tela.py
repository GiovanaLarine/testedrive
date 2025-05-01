from testedrive.cmdline.componentes.mensagens import mostrar_titulo


def tela_menu_principal():
    mostrar_titulo("Sistema de Agendamentos")
    print("1 - Gerenciar Agendamentos")
    print("2 - Gerenciar Clientes")
    print("3 - Catálogo de Veículos")
    print("4 - Catálogo de Rotas")
    print("0 - Sair")
    
    return input("\nEscolha uma opção: ")
