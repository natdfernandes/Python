class Pessoa:
    def __init__(self, nome, endereco) -> None:
        self.set_nome(nome)
        self.set_endereco(endereco)

    def set_nome(self, nome):
        self.nome = nome

    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_nome(self):
        return self.nome

    def get_endereco(self):
        return self.endereco
    def apresentar_pessoa(self):
        print(f'nome:{self.get_nome()}, endereço:{self.get_endereco()}')
    
class Bebe(Pessoa):
    def __init__(self, nome, endereco, meses) -> None:
        super().__init__(nome, endereco)
        self.meses = meses
    
    def get_meses(self):
        return self.meses
    
    def apresentar_pessoa(self):
        print("gugu dada")
### === programa principal === ###

pessoa1= Pessoa("Nat", "123")
pessoa2= Pessoa("Leo", "456")

pessoa1.apresentar_pessoa()
pessoa2.apresentar_pessoa()
pessoa2.set_endereco('123')
pessoa2.apresentar_pessoa()

bebe1 = Bebe("nenem", "231", 2)
print(bebe1.get_meses())
bebe1.apresentar_pessoa()
