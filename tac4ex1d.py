#1 - Faça um programa que leia um número indeterminado de valores e
#armazene numa lista, correspondentes a notas, encerrando a entrada de
#dados quando for informado um valor igual a -1 (que não deve ser armazenado).

lista = []


while True:
	n = int(input('Digite um numero:'))
	if(n == -1):
		break
	else:
		lista.append(n)

print(lista)


#d) Uma função que calcule e mostre a soma dos valores


def calculaSoma(lista):
    soma=0
    for numerodalista in lista:
        soma+=numerodalista
    return soma

print('A soma dos valores é:',calculaSoma(lista))
