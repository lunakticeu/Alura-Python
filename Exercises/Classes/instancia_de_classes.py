class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_yakissoba = Restaurante()

#1 Atribua o valor 'Chinesa' ao atributo categoria da instância restaurante_yakissoba da classe Restaurante.
restaurante_yakissoba.categoria = 'Chinesa'

#2 Acesse o valor do atributo nome da instância restaurante_yakissoba da classe Restaurante.
nome_do_restaurante = restaurante_yakissoba.nome

#3 Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_yakissoba.ativo:
    print('Restaurante ativo')
else:
    print('Restaurante inativo')

#4 Acesse o valor do atributo de classe categoria diretamente da classe Restaurante.
categoria = Restaurante.categoria

#5 Altere o valor do atributo nome para 'Bistrô'.
restaurante_yakissoba.nome = 'Bistrô'

#6 Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

#7 Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
   print('A categoria não é Fast Food.')

#8 Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

#9 Imprima no console o nome e a categoria da instância restaurante_yakissoba.
print(f'Nome: {restaurante_yakissoba.nome}, Categoria: {restaurante_yakissoba.categoria}')
