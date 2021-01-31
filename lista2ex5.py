#5
#Faça um algoritmo para ler
#três números positivos e escrevê-los em ordem crescente.

a= int(input('Digite um numero inteiro e positivo:'))
b= int(input('Digite outro numero inteiro e positivo:'))
c= int(input('Digite outro numero inteiro e positivo:'))

print (" ordem antes era %d , %d , %d "  % (a,b,c))
print('A ordem agora é:')


ordem=[a,b,c]
print(sorted(ordem))
