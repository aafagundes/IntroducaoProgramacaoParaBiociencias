#3 - Escreva um código em Python que leia um número e verifique se é ou não
#um número primo. Para fazer essa verificação, calcule o resto da divisão
#do número por 2 e depois por todos os números ímpares até o número lido.
#Lembre-se que 0 e 1 não são primos e 2 é o único par primo.

b=0
n = int(input('digite um numero:'))

for c in range(1, n+1):
    if n % c == 0:
        b += 1

         
if b == 2:
    print('É um numero primo')

    
else:
    print('Não é um numero primo')
