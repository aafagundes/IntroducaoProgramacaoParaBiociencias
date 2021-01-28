#1
#Escreva um código em Python para ler o nome, as três notas e o número de faltas
#de um aluno e escrever qual a sua situação final:
#Aprovado, Reprovado por Falta ou Reprovado por Média.
#A média para aprovação é 7,0 e o limite de faltas é 25%
#do total de aulas. O número de aulas ministradas no semestre foi de 80.
#A reprovação por falta sobrepõe a reprovação por Média.
#presença precisa ser maior que 60


nome= input('nome do aluno:')

nota1= float(input('digite a primeira nota:'))
             
nota2 = float(input('digite a segunda nota:'))
            
nota3= float(input('digite a terceira nota:'))
            
aulas = int(input('quantas presenças em aulas?'))



media=  (nota1+nota2+nota3)/3
print('a media do aluno foi de %2.f' % media)

if aulas<60:
    print('%s foi reprovado por falta' % nome)


if media< 7.0:
    print('%s foi reprovado por media' % nome)

elif media>= 7.0 and aulas>=60:
    print('%s foi aprovado' % nome)


