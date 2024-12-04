
# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro():
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meuCarro = Carro('Fiat', 'Azul', 2022)
print(vars(meuCarro))
 

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante():
    def __init__(self, nome, categoria, vendas, capacidade, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.vendas = vendas
        self.capacidade = capacidade
        self.ativo = ativo
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
# Instanciando um restaurante e atribuindo valores aos seus atributos
meuRestaurante = Restaurante('Comida Boa', 'Gourmet', 1500, 50, True)

# Crie uma classe chamada `Cliente` e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')