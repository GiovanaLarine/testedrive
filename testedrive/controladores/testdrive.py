from flask import Blueprint, render_template

testdrive = Blueprint("testdrive", __name__)

# HTTP GET -> nissan.com/
@testdrive.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("pagina_inicial.html")

 