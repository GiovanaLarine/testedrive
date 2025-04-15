from testedrive.modelos.cliente_modelo import Cliente

class ClienteServico:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def cadastrar_cliente(self, nome, sobrenome, email, cpf):
        cliente = Cliente(nome=nome, sobrenome=sobrenome, email=email, cpf=cpf)
        self.repositorio.adicionar(cliente)
        return cliente