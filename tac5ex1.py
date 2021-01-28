#1 - Escreva um programa Python que peça ao usuário uma sequência de DNA
#e imprima a sequência de mRNA e a sequência de proteína correspondentes.


from Bio.Seq import Seq

stringSeq=(input('digite uma sequencia de DNA:')).upper()
sequencia= Seq(stringSeq)
sequenciarna= sequencia.transcribe()
sequenciaproteinas= sequenciarna.translate()
print(f'RNA:{sequenciarna},  PROTEINA:{sequenciaproteinas}')

# ou dna = "GATGGAACTTGACTACGTAAATT"
#rna = dna.replace ("T", "U")
