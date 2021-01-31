#4
#Escreva um programa que leia dois números e que pergunte qual operação
#deseja realizar. Você deve poder calcular a soma (+), subtração (-),
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada

numero1=int(input("digite o primeiro numero:"))

numero2=int(input("digite o segundo numero:"))

print("digite o numero da operacao que voce deseja:")
print("1 para soma")
print("2 para subtracao")
print("3 para divisao")
print("4 para multiplicacao")

operacao= int(input("operacao numero="))

if operacao == 1:
    resultado=(numero1+numero2)

elif operacao == 2:
   resultado= (numero1-numero2)
    
elif operacao == 3:
   resultado= (numero1/numero2)

elif operacao == 4:
    resultado=(numero1*numero2)

else:
    print("Operacao invalida")
    resultado= "erro"

    
print(resultado)
