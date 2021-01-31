#2 - Escreva um código em Python que efetue a soma de todos os números
#ímpares que são múltiplos de três e que se encontram no conjunto dos
#números de 1 até 500.

soma=0


for c in range (1,501,2):
    if c % 3 == 0:
        soma = soma + c
print('A soma dos numeros impares e multiplos de 3 é %d' % soma)
    
