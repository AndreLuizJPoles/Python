#Conjectura de Collatz
#Entrada de dados
num = int(input("Escreva um número:"))
i=0
#Operacao
while num != 1:
    if num%2 == 1:
        num = 3*num+1
    else:
        num/=2
    i+=1
print("Número final: %d\n Número de contas realizadas: %d\n"%(num, i))