class ClienteRepositorio:
    def __init__(self, session):
        self.session = session

    def adicionar(self, cliente):
        self.session.add(cliente)
        self.session.commit()