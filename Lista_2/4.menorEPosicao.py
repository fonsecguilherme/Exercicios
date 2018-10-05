a = int(input("Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Teceiro: "))
d = int(input("Quarto: "))
e = int(input("Quinto: "))

lista = [a,b,c,d,e]
print(lista)
menor = min(lista, key = int)  
posi = lista.index(menor)  
print("O menor é: " +str(menor))
print("Posição: " +str(posi+1))