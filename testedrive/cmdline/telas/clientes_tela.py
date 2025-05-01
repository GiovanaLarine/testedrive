from testedrive.cmdline.componentes.mensagens import mostrar_titulo

def tela_menu_clientes():
    mostrar_titulo("Menu Clientes")
    print("1 - Cadastrar um cliente")
    print("2 - Buscar um cliente")
    print("3 - Listar clientes")
    print("0 - Voltar")

    return input("Escolha uma opção: ")

def tela_cadastrar_cliente():
    print("Cadastrar cliente\n")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("Email: ")
    cpf = input("CPF: ")

    return {"nome": nome, "sobrenome": sobrenome, "email": email, "cpf": cpf}

