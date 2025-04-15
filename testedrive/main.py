from testedrive.dominio.repositorios.cliente_repositorio import ClienteRepositorio
from testedrive.dominio.servicos.cliente_servico import ClienteServico
from testedrive.db import Session
from testedrive.modelos.cliente_modelo import Cliente

def main():
    print("Cadastrar cliente\n")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("Email: ")
    cpf = input("CPF: ")

    with Session() as session:
        repositorio = ClienteRepositorio(session)
        servico = ClienteServico(repositorio)

        cliente = servico.cadastrar_cliente(nome, sobrenome, email, cpf)
    
    print(f"Cliente: {cliente.nome} cadastrado!")

if __name__ == "__main__":
    main()