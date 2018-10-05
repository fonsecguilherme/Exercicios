numero = int(input("Digite o numero a ser verificado: "))
divisor = 1
contador = 0

while divisor < numero:
    if numero % divisor == 0:
        contador += 1
    divisor += 1

if contador > 1:
    print("Não é primo")
else:
    print("É primo")
