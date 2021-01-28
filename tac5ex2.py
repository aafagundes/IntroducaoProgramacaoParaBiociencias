
#2 - Escreva um programa em Python que recebe uma sequência de DNA do
#usuário e calcula o conteúdo GC da sequência sem usar Biopython, ou seja,
#crie um código que conte a quantidade de cada caractere na sequência de DNA
#e mostre o porcentagem de (G+C)*L, onde L é o tamanho da sequência. Para
#comparar o resultado, calcule o conteúdo GC usando um método do Biopython
#explicado em aula.


from Bio.Seq import Seq
from Bio.SeqUtils import GC, nt_search
CmaisG=0

stringSeq=(input('digite uma sequencia de DNA:')).upper()
L=len(stringSeq)
sequencia=Seq(stringSeq)

for letra in sequencia:
    if letra == 'C' or letra == 'G':
        CmaisG += 1


porcentagem=((CmaisG)/L)*100        


print(porcentagem)
print(GC(sequencia))
