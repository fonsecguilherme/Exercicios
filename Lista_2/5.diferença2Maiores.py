import heapq

a = int(input("Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Teceiro: "))
d = int(input("Quarto: "))
e = int(input("Quinto: "))

lista = [a, b, c, d, e]
print("Lista original: " + str(lista))
print("Dois maiores: " + str(heapq.nlargest(2, lista)))
maior = max(lista, key=int)
posi = lista.index(maior)
del lista[posi]
maior2 = max(lista, key=int)
print("Diferença dois maiores: " + str(maior - maior2))
