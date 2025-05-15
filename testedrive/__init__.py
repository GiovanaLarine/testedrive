from flask import Flask
from testedrive.controladores import testdrive
from driveui import setup_theme

# Factory -> Fabrica do app
def create_app():
    app = Flask(__name__, template_folder="paginas")
    setup_theme(app)

    app.register_blueprint(testdrive)

    return app