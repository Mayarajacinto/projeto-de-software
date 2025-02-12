mesagem = 'Olá, mundo!'
print (mesagem) #ou
print('Olá, mundo!')

idade = 21
nome = 'mayara'
print('Meu nome é', nome, 'e tenho', idade, 'anos')
print('Meu nome é {0} e tenho {1} anos' .format(nome, idade))
print(f'nome: {nome}\t idade: {idade}')

nome2 = input('Digite seu nome:')
print('olá ' + nome2 + 'bem vindo!')

print('Com quebra de linha')
print('Sem quebra de linha', end='')
print(' permaneço na mesma linha')

a = 4
b = 7
print(f'A soma de {a} + {b} é {a+b}')

valor = 3.14959
print(f'O valor é {valor:.2f}')
print(f'O valor é \'{valor:.3f}\'')