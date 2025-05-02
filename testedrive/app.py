from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html")


@app.route("/agendamentos", methods=["GET"])
def listar_agendamentos():
    return render_template("listar-agendamentos.html")

if __name__ == "__main__":
    app.run()
# www.nissan.com.br/agendamentos/criar
# Rota ou Caminho-> /agendamentos/criar

# CRUD -> CREATE(CRIAR), READ (LER), UPDATE (ATUALIZAR), DELETE (DELETAR)
# GET -> Pedir alguma coisa == READ
# POST -> Enviar alguma coisa == CREATE
# Possui 2 rotas até agora:
#     - nissan.com.br/
#     - nissan.com.br/agendamentos



