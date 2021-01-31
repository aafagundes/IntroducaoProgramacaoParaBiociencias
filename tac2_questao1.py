#tac2_questao1



diaria = float(input("quantos dias usou o servidor?"))
terabytes= float(input("quantos terabytes usou?"))



quantidadebytes= terabytes * (10**6)



valorArmazenamento= quantidadebytes * 0.05

valorDiaria= diaria * 40.00



valorTotal = valorArmazenamento + valorDiaria

print(f'gastara no total: {valorTotal} reais')

