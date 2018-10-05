a = int(input("Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Teceiro: "))

lista = [a, b, c]

maior = max(lista, key=int)
posiMaior = lista.index(maior)
del lista[posiMaior]
menor = min(lista, key=int)
posMenor = lista.index(menor)
del lista[posMenor]
print("O valor intermediario é: " + str(lista))
