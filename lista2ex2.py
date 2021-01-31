#2
# Faça um algoritmo para ler dois números inteiros e informar
#se estes números são iguais ou diferentes, maior ou menor que o outro.


num1 = int(input('Digite um numero:'))
num2= int(input('Digite outro numero:'))

if num1 == num2:
    print('Os numeros sao iguais')

elif num1 != num2:
    print('Os numeros sao diferentes')

if num1>num2:
    print('O primeiro numero é maior')

if num1<num2:
    print('O segundo numero é maior')
