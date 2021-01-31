#3
#Faça um algoritmo para ler duas variáveis inteiras A e B e
#garantir que A e B fiquem em ordem crescente, ou seja, a variável A
#deverá armazenar o menor
#valor fornecido e a variável B o maior

a=int(input("digite variavel A:"))
b=int(input("digite variavel B:"))


auxiliar=0

if a > b:
    print ("A antes = %d" % a)
    auxiliar=a
    a = b
    print("A depois = %d" % a)    
    b=auxiliar
    print("B depois = %d" % b)

#imprime A e B

print(a)
print(b)
        
