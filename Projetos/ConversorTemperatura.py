# Auxiliares
tipo = 0
converter = 0
# Entrada de Dados
while tipo != 1 and tipo != 2 and tipo != 3:
    tipo = int(
        input("Insira a unidade de medida(1=Celsius, 2=Fahrenheit e 3=Kelvin):"))
    if 0 <= tipo >= 4:
        print("Insira uma das opções")
temperatura = float(input("Insira o valor da temperatura: "))
while converter != 1 and converter != 2 and converter != 3:
    if 0 <= converter >= 4:
        print("Insira uma das opções")
    converter = int(
        input("Insira a unidade de medida para que será convertida (1=Celsius, 2=Fahrenheit e 3=Kelvin):"))

# Contas e Impressão
if tipo == 1 and converter == 1:
    print("A temperatura é de %.2f°C" % (temperatura))
elif tipo == 2 and converter == 2:
    print("A temperatura é de %.2f°F" % (temperatura))
elif tipo == 3 and converter == 3:
    print("A temperatura é de %.2f°K" % (temperatura))
elif tipo == 1 and converter == 2:
    resp = 1.8 * temperatura + 32
    print("A temperatura é de %.2f°F" % (resp))
elif tipo == 2 and converter == 1:
    resp = (temperatura - 32)/1.8
    print("A temperatura é de %.2f°C" % (resp))
elif tipo == 1 and converter == 3:
    resp = temperatura + 273.15
    print("A temperatura é de %.2f°K" % (resp))
elif tipo == 3 and converter == 1:
    resp = temperatura - 273.15
    print("A temperatura é de %.2f°C" % (resp))
elif tipo == 2 and converter == 3:
    resp = (temperatura - 32)/1.8
    resp = resp + 273.15
    print("A temperatura é de %.2f°K" % (resp))
elif tipo == 3 and converter == 2:
    resp = temperatura - 273.15
    resp = 1.8 * resp + 32
    print("A temperatura é de %.2f°F" % (resp))
