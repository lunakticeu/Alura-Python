class Contador:
    '''
    Classe que representa um contador.
    A instância mantém um contador específico, enquanto um contador global é compartilhado por todas as instâncias.
    '''

    contador_global = 0

    def __init__(self):
        self.valor = 0

    def __str__(self):
        return f'Contador: {self.valor}'

    def incrementar(self):
        self.valor += 1

    @classmethod
    def zerar_contador_global(cls):
        cls.contador_global = 0
        return 'Contador global foi zerado.'

print(Contador.contador_global)
contador1 = Contador()
print(contador1)
contador1.incrementar()
print(contador1)
contador2 = Contador()
print(contador2)
contador2.incrementar()
print(contador2)
print(Contador.contador_global)