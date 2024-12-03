'''
Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC
e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
'''

peso = float(input('Digite o seu peso em Kgs: '))
altura = float(input('Digite a sua altura em metros: '))
imc = round(peso / (altura ** 2), 2)

print(f'IMC: {imc}')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso normal')
else:
    print('Acima do peso')