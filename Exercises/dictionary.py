'''
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

2 - Utilizando o dicionário criado no item 1:
Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.

3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
'''

person = {"name": "Luna", "age": 24, "city": "Rio de Janeiro"}
print(person)
# Modifique o valor de um dos itens no dicionário
person["age"] = 30
print(person)

# Adicione um campo de profissão para essa pessoa
person["profession"] = "Baba"
print(person)

# Remova um item do dicionário
del person["city"]
print(person)

# Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5
numbers = {}
for i in range(1, 6):
    numbers[i] = i * i
print(numbers)

# Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário
person = {"name": "Luna", "age": 24, "city": "Rio de Janeiro"}
text = input("Enter a key: ")
if text in person:
    print(f"The key {text} exists in the dictionary")
else:
    print(f"The key {text} does not exist in the dictionary")

# Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário
phrase = "You're my sunshine, my only sunshine"
words = phrase.replace(",", "").split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)

# A funcionalidade deve percorrer uma lista de livros e exibir o nome de cada livro disponível em estoque. No entanto, se o livro estiver esgotado, ele deve ser ignorado durante a iteração.
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] > 0:
        print(f"Livro disponível: {livro['nome']}")    
