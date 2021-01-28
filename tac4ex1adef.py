#1 - Faça um programa que leia um número indeterminado de valores e
#armazene numa lista, correspondentes a notas, encerrando a entrada de
#dados quando for informado um valor igual a -1 (que não deve ser armazenado).
lista = []
while True:
	n = int(input('Digite um numero ou (-1) para parar:'))
	if(n == -1):
		break
	else:
		lista.append(n)
print(lista)

#a)Uma função que mostre a quantidade de valores que foram lidos;

def QuantidadeValores(lista):
    return len(lista)

print('A quantidade de valores da lista é:',QuantidadeValores(lista))


#b) Uma função que mostre todos os valores na ordem em que foram informados,
#um ao lado do outro;

def mostrarValoresNaOrdemDeLeitura(lista):
    return str(lista).strip('[]')

print('Na ordem de leitura a lista fica:', mostrarValoresNaOrdemDeLeitura(lista))


#c)Uma função que mostre os valores na ordem inversa à que foram informados,
#um abaixo do outro

def mostrarValoresNaOrdemInversaDeLeitura(lista):
   lista.reverse()
   for i in range(len(lista)):
       print(lista[i])

print('Na ordem inversa fica:')
mostrarValoresNaOrdemInversaDeLeitura(lista)


#d) Uma função que calcule e mostre a soma dos valores

def calculaSoma(lista):
    soma=0
    for numerodalista in lista:
        soma+=numerodalista
    return soma
print('A soma dos valores é:',calculaSoma(lista))


#e)  Uma função que calcule e mostre a média dos valores;
def calculaMedia(lista):
        return(calculaSoma(lista)/QuantidadeValores(lista))

print('A media dos valores da lista é:',calculaMedia(lista))



#f) Uma função que calcule e mostre a quantidade de valores acima da média
#calculada;
def mostrarValoresAcimaMedia(lista):
    nAcima=0
    for valor in lista:
       if valor>calculaMedia(lista):
           nAcima += 1
    return(nAcima)

print('A quantidade de valores acima da média é de:',mostrarValoresAcimaMedia(lista))
        






