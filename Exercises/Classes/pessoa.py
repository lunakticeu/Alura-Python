'''
Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
Adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
'''

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Olá {self.nome}, voce tem {self.idade} anos e trabalha como {self.profissao}'

    def aniversario(self):
        self.idade += 1
        return self.idade

    @property
    def saudacao(self):
        if self.profissao == '':
            return f'Saudações {self.nome}, voce tem {self.idade} anos'
        else:
            return f'Saudações {self.nome}, voce tem {self.idade} anos e trabalha como {self.profissao}'

pessoa1 = Pessoa('Luna primeira', 24, 'Babá')
pessoa2 = Pessoa()
pessoa3 = Pessoa('Luna terceira', 34)

# Imprimindo informações iniciais
print(pessoa1)
print(pessoa2)
print(pessoa3)

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa3.aniversario()
print(pessoa3.saudacao)