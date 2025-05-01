from testedrive.modelos.cliente_modelo import Cliente

class ClienteServico:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def cadastrar_cliente(self, dto):
        cliente = Cliente(nome=dto.nome, sobrenome=dto.sobrenome, email=dto.email, cpf=dto.cpf)
        self.repositorio.adicionar(cliente)
        return cliente