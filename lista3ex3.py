#3 - Escreva um código em Python para contar a quantidade
#de números pares entre dois números quaisquer.

n=int(input('digite um numero:'))
f=int(input('digite outro numero maior:'))

if n>=f:
    print('voce digitou a ordem errada')


cont=0

for c in range (n,f):
    if c % 2 == 0:
        cont = cont + 1
        
print('A quantidade de numeros pares entre os dois numeros é %d' % cont)
