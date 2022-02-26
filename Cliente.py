import random

class Cliente:
    anoAtual = 2021

    #Self: Pode ser qualquer outra palavra, usada pra entender que é esse objeto.
    #__init__: método pra criar o objeto e os seus Atributos.
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    @property
    def getNome(self):
        return self.nome

    @getNome.setter
    def setNome(self, nome):
        self.nome = nome
    
    @property
    def getIdade(self):
        return self.idade

    @getIdade.setter
    def setIdade(self, idade):
        self.idade = idade
    
    @property
    def getCpf(self):
        return self.cpf
    
    @getCpf.setter
    def setCpf(self, cpf):
        self.cpf = cpf

    #Método que utiliza dos valores da instancia
    def getAnoNascimento(self):
        return (self.anoAtual - self.idade)

    #Método global da classe
    #cls: Pode ser outro nome, refere-se a classe
    @classmethod
    def instanciaPorAno(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade)
    
    #Método que não precisa nem do Self nem Cls
    @staticmethod
    def geraId():
        return random.radint(10000, 19999)