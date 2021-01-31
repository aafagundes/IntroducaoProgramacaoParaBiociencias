#5 - Escreva um código em Python que o usuário digite vários
#números inteiros e positivos e imprima o produto dos números
#ímpares e a soma dos números pares.


soma=0
produto=1


n = int(input('digite um numero:'))


while True:
    if n % 2 == 0:
        soma= soma + n
    else:
        produto= produto * n


    print(soma)
    print(produto)
    n = int(input('digite outro numero:'))
      


