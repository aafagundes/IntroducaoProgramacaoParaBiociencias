#3- Escreva um código que leia uma frase digitada pelo usuário. Em seguida, escreva: 
# a - uma função lambda que identifique quando um caractere é uma vogal
# b - uma função lambda que identifique quando um caractere é uma consoante
# c - uma função lambda identifique quando um caractere é um número


vogais = lambda caractere: caractere.upper() in 'AEIOU'

consoantes= lambda caractere: caractere.upper() in 'BCDFGHJKLMNPQRSTWYZ'

numeros= lambda caractere: caractere in '123456790'


frase= input('Digite uma frase: ')

totvogais=0
totconsoantes=0
totnumeros=0
totetc=0


for caractere in frase:
    if vogais(caractere):
        totvogais+=1
    elif consoantes(caractere):
        totconsoantes+=1
    elif numeros(caractere):
        totnumeros+=1
    else:
        totetc+=1


print(f'O total de vogais é de {totvogais} na frase')
print(f'O total de consoantes é de {totconsoantes} na frase')
print(f'O total de numeros é de {totnumeros} na frase')
print(f'O total de outros caracteres na frase é de {totetc}')
