#Entrada dos dados
operador = 'a'
while operador != '+' and operador != '-' and operador != '/' and operador!= '*':
    operador = input('Escreva a operacao(* - + /):')
    if operador != '+' and operador != '-' and operador != '/' and operador!= '*':
        print('Insira operacao valida!')
num1 = float(input('Escreva o primeiro valor: '))
num2 = float(input('Escreva o segundo valor: '))
#Realizar Operação
if operador == '*':
    resultado = num1 * num2
    print('Resultado: %f' %(resultado))
elif operador == '-':
    resultado = num1 - num2
    print('Resultado: %f' %(resultado))
elif operador == '+':
    resultado = num1 + num2
    print('Resultado: %f' %(resultado))
elif operador == '/':
    resultado = float(num1/num2)
    print('Resultado: %f' %(resultado))