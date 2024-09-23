class Pessoa:
    #metodo construtor
    def __init__(self, Nome, idade, comendo=False, falando=False):
        self.nome = Nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        #metodo simples
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome}já está comendo.')  
            return
        print(f'{self.nome} com a idade de {self.idade} anos, está comendo {alimento}. ')  
        self.comendo = True
    #metodo simples
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} nao esá comendo.')
            return
    #metodo simples
    def falar (self):
        print('a pessoa está falando...')
        
nat = Pessoa("Natalia", 23)
print(nat.nome)
nat.comer("bolo de cenoura")
leo = Pessoa("Leonardo", 26)
leo.comer("sorvete")
leo.falar()
nat.parar_comer()