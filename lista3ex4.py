#4 - Escreva um código em Python que leia números inteiros do teclado.
#O programa deve ler os números até que o usuário digite 0 (zero).
#No final da execução, exiba a quantidade de números digitados,
#assim como a soma e a média aritmética

soma = 0

n=int(input('digite um numero:'))

nlidos=0

while n != 0:
    soma = soma + n
    nlidos= nlidos + 1
    n=int(input('digite outro numero:'))

print('A soma dos numeros é %d ' % soma)


media= soma/nlidos
print('A media é %2.f ' %media)
