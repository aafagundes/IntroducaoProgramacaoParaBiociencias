#6 - Escreva um código em Python que leia a altura de 15 pessoas.
#Este programa deverá calcular e mostrar : 
#a. A menor altura do grupo; 
#b. A maior altura do grupo;



alturaslidas = 1
altura= float(input('digite a altura:'))


maioraltura = altura
menoraltura = altura


for i in range(14):
    altura=float(input('digite a altura:'))
    if altura > maioraltura:
        maioraltura = altura
    if altura< menoraltura:
        menoraltura = altura
        
print(maioraltura)
print(menoraltura)
