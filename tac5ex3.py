#3 - Escreva um programa Python que peça ao usuário duas sequências de DNA
#e imprima o complemento reverso de sua concatenação sem usar Biopython.
#Em seguida, faça o mesmo usando os métodos do Biopython para comparar o
#resultado.

from Bio.Seq import Seq
from Bio.SeqUtils import GC, nt_search


stringSeq1=(input('digite uma sequencia de DNA:')).upper()
stringSeq2=(input('digite outra sequencia de DNA:')).upper()

string=stringSeq1+stringSeq2
sequencia=Seq(string)
rev= sequencia.reverse_complement()
print(rev)

