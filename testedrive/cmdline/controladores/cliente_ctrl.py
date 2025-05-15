from testedrive.cmdline.componentes.mensagens import mostrar_sucesso
from testedrive.db import Session
from testedrive.dto.cliente_dto import ClienteDTO
from testedrive.dominio.servicos.cliente_servico import ClienteServico
from testedrive.dominio.repositorios.cliente_repositorio import ClienteRepositorio
from testedrive.cmdline.telas.clientes_tela import tela_cadastrar_cliente


def cadastrar_cliente():
    dados = tela_cadastrar_cliente()
    # DTO -> Data Transfer Objetc -> Objeto para transferir dados
    cliente_dto = ClienteDTO(
        nome=dados["nome"],
        sobrenome=dados["sobrenome"],
        email=dados["email"],
        cpf=dados["cpf"],
    )
    with Session() as session:
        repositorio = ClienteRepositorio(session)
        servico = ClienteServico(repositorio)

        cliente = servico.cadastrar_cliente(cliente_dto)
        mostrar_sucesso(f"Cadastro de {cliente.nome} concluido!")
