class Portfel:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def wplac(self, ile:int):
        self.saldo += ile

class NiewystarczajaceSrodki(Exception):
    pass
