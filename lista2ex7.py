#7
#Escreva um programa que pergunte a velocidade do carro de um usuário.
#Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h.

vel= int(input('Qual a velocidade do carro?'))

if vel<=80:
    print('Voce nao foi multado')


elif vel > 80:
    excedido= vel-80
    multa= excedido * 5
    print('Voce foi multado, no valor de %d reais' %multa)

 
