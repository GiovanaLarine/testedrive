from testedrive.cmdline import cli
from testedrive.modelos import registrar_modelos

def main():
    registrar_modelos()
    cli()
    # MVC -> Model, View e Controller -> Modelo, Apresentação, Controlador
    # CLI -> CMDLINE -> Command Line -> Linha de Comando
    # Como a interface para interagir com o programa é via Terminal
    # Então a função cli() é a camada View do MVC
    


if __name__ == "__main__":
    main()
