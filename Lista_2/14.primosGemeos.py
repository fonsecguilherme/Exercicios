import sys


def verificaPrimo(num):
    divisor = 1
    contador = 0
    while divisor < num:
        if num % divisor == 0:
            contador += 1
        divisor += 1

    if contador > 1:
       return False
    else:
        return True


numero = int(input("Digite o numero a ser verificado: "))
numero2 = int(input("Digite o próximo numero a ser verificado: "))
lista = [numero, numero2]

if verificaPrimo(numero) == verificaPrimo(numero2): 
        maior = max(lista, key = int)
        menor = min(lista, key = int)
        if maior - menor == 2:
            print("Primos gêmos")
        else:
            print("São primos, mas não gêmeos")
else: 
    print("Um dos dois números não é primo")
