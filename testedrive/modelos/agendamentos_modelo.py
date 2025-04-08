class Agendamento(Model):
    __tablename__ = "agendamentos"

    id = mapped_column(Integer, primary_key=true)
    