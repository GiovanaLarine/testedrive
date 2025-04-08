from testedrive.db import Model

class Veiculo(Model):
    __tablename__ = "veiculos"

    id = mapped_column(Integer, primary_key=True)
    marca = mapped_column(String(50), nullable=False)
    modelo = mapped_column(String(100), nullable=False)
    ano = mapped_column(Integer, nullable=False)
    motor = mapped_column(String(20), nullable=True)
    combustivel = mapped_column(String(20), nullable=True)
    ativo = mapped_column(Boolean, default=True)

    rotas = relationship("RotaVeiculo", back_populates="veiculo")
