#simples, composto e encadeado

media = 0.0
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

media = (n1 + n2) / 2

if(media >= 7.0): print('Aprovado')
elif(media >=6.0 and media < 7.0): print('Recuperação')
else: print('Reprovado')

print ('Média: {}' .format(media))
print ('media ', media)

