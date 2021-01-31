#1 - Escreva um código que contenha uma função que recebe como parâmetro
#uma string, o número mínimo e número máximo de caracteres. A função retorna
#verdadeiro se o comprimento da string está entre o intervalo mínimo e máximo
#de caracteres. Caso contrário, imprime falso.


def frase(string,minimo,maximo):
    if minimo <= len(string) <= maximo:
        return True
    else:
        return False

print(frase('frase teste falso', 2,5))


print(frase('frase teste verdadeira', 2,50))


print(frase('frase teste 2 falsa', 60,100))
