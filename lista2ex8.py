#8
#Escreva um algoritmo que leia o número de identificação, as
#3 notas obtidas por um aluno nas 3 provas e a média dos exercícios
#que fazem parte da avaliação, e calcule a média de
#aproveitamento, usando a fórmula 
#MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7



ident = int(input('Numero de identificacao do aluno:'))

nota1= float(input('primeira nota foi:'))
nota2= float(input('segunda nota foi:'))
nota3= float(input('terceira nota foi:'))

me= float(input('digite a media dos exercicios:'))

mediaApr= (nota1 + nota2 * 2 + nota3 * 3 + me)/7


print('O numero de identificacao do aluno é %d , Suas notas foram %.2f , %.2f , %.2f' % (ident , nota1 , nota2 , nota3))
print('Sua media de exercicios foi %.2f , Sua media de aproveitamento foi %.2f e Seu conceito foi:' % (me , mediaApr))

if mediaApr >= 90:
    print('A-aprovado')

elif mediaApr >= 75:
    print('B-aprovado')

elif mediaApr >=60:
    print('C-aprovado')

elif mediaApr >=40:
    print ('D-reprovado')

else:
    print('E-reprovado')

    

        
