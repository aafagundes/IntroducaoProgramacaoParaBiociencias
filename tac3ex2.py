#2
#O IMC – Indice de Massa Corporal é um critério da Organização Mundial de
#Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta.
#A fórmula é IMC = peso/(altura)². Escreva um código em Python que leia o peso e a altura de um adulto e mostre sua condição de acordo com a
#tabela abaixo.


peso= float(input('digite o peso:'))

altura= float(input('digite a altura:'))

imc= peso/(altura)**2
print('o imc é %3.f' % imc)

if imc<18.5:
    print('O peso é de %2.f , a altura de %2.f , o imc indica que esta abaixo do peso' % (peso,altura))

elif imc >= 18.5 and imc<25:
    print('O peso é de %2.f , a altura de %2.f , o imc indica peso normal'% (peso,altura))

elif imc >=25 and imc < 30:
     print('O peso é de %2.f , a altura de %2.f , o imc indica que esta acima do peso'% (peso,altura))

elif imc>=30:
    print('O peso é de %2.f , a altura de %2.f , o imc indica que esta obeso'% (peso,altura))
    
