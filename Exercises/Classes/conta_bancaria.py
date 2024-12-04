'''
1- Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
2- Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
3- Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
4- Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
5- Crie uma instância da classe e imprima o valor da propriedade titular.
6- Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
7- Crie um método de classe para a conta ClienteBanco.
'''
class ContaBancaria:
    def __init__(self, titular, saldo, ativo=False):
        self.titular = titular
        self.saldo = saldo
        self._ativo = ativo

    def __str__(self):
        return f'Titular: {self.titular}, Saldo: {self.saldo}, Ativo: {self._ativo}'

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta1 = ContaBancaria('João', 1000)
conta2 = ContaBancaria('Maria', 500)

print(conta1)
print(conta2)

# use classmethod ativar_conta
conta1.ativar_conta(conta1)
print(conta1)

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Titular: {self.titular}, Saldo: {self.saldo}, Ativo: {self._ativo}'

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

conta3 = ContaBancariaPythonica('Paulo', 3000)
print(f"Titular da conta 3: {conta3.titular}")

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
    
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Estudante")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Pintora")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Advogado")

# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")


