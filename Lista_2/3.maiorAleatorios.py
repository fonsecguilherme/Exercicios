a = int(input("Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Teceiro: "))
d = int(input("Quarto: "))
e = int(input("Quinto: "))

lista = [a,b,c,d,e]
print(lista)
maior = max(lista, key = int)    
print("O maior é: " +str(maior))

#maior = max(listaFinal, key = float)
#print("O maior é: " +str(maior))
