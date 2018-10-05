num = int(input("Digite o número a ser verificado: "))
divisor = 1
lista = []

while num > divisor:
    if num % divisor == 0: 
        lista.append(divisor)
    divisor += 1

print("Divisores: " +str(lista))
resultado = sum(lista)

if resultado == num: 
    print("É n perfeito.")
else: 
    print("Não é n perfeito. ")