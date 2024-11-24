# Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
def par_impar():
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')

# Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de
# acordo com as seguintes condições: Criança: 0 a 12 anos; Adolescente: 13 a 18 anos; Adulto: acima de 18 anos.
def classificar_idade():
    idade = int(input('Qual é a sua idade? '))
    if idade <= 12:
        print(f'Voce tem {idade} anos, é uma CRIANÇA')
    elif 13 <= idade <= 18:
        print(f'Voce tem {idade} anos, é um ADOLESCENTE')
    else:
        print(f'Voce tem {idade} anos, é um ADULTO')

# Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar
# se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

def validar_credenciais():
    nome = str(input('Digite o nome de usuário: '))
    senha = int(input('Digite a senha: '))
    if nome == 'luna' and senha == 123:
        print('Usuário e senha correto')
    else:
        print('Usuário e senha incorreto')

'''Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
    Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
    Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
    Caso contrário: o ponto está localizado no eixo ou origem.
'''
def definir_coordenadas():
    x = int(input('Digite a coordenada de x: '))
    y = int(input('Digite a coordenada de y: '))
    if x > 0 and y > 0:
        print(f'Primeiro Quadrante: X é {x} e Y é {y}, sendo maiores que zero')
    elif x < 0 and y > 0:
        print(f'Segundo Quadrante: X é {x} e Y é {y}, sendo x menor que zero e y maior que zero')
    elif x < 0 and y < 0:
        print(f'Terceiro Quadrante: X é {x} e Y é {y}, sendo menores que zero')
    elif x > 0 and y < 0:
        print(f'Quarto Quadrante: X é {x} e Y é {y}, sendo x maior que zero e y menor que zero')
    else:
        print('Ponto esta localizado no eixo ou origem')

definir_coordenadas()



