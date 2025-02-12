# cntrl sfith aspas -> abre o terminal
# para comando interativos no terminal ->py
# + soma
# - subtração 
# * multiplicação
# / divisão real 
# // divisão inteira
# ** potenciação
# % módulo ou resto da divisão

x = 10
y = 3

print('1. a soma é', x+y)

#input retorna a uma string, para converter para int ou float, é necessário fazer a conversão
x = input('Digite um número: ')
y = input('Digite outro número: ')

print('2.a soma é', x+y) #concatenação, com outras operações não é possível

x = int(input('digite um numero:'))
y = int(input('digite outro numero:'))

print('3.a soma é', x+y)

# = atribuição
# == igual a 
# != diferente de
# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a

x = y = z = False #valores logicos 
n1 = n2 = 0

print('digite um número:')
n1 = int(input())
n2 = int(input('digite outro número:'))

x = n1 == n2 # x tem o valor de True ou False, operadores logicos 
print('são iguais?', x, '\n')

z = n1 > n2 # z tem o valor de True ou False
print(n1, 'é maior que', n2, '?', z, '\n')

y = n1 != n2

#print('são diferentes?'+ y, '\n') erro, não é possível concatenar string com booleano, a virgula permite a concatenação
print('são diferentes?' + str(y), '\n')


#and, or, not -> operadores lógicos

idade = 19
altura = 1.75

#(idade >= 18) equivale a uma pergunta com resposta True ou False
resultado = (idade >= 18) and (altura >= 1.70)
mensagem = 'Pode entrar?' + str(resultado)
print(mensagem)  #resultado booleano

temDinheiro = False 
msg = 'tem dinheiro?' + str(not temDinheiro)
print(msg)