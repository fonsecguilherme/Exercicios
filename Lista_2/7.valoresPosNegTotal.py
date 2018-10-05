a = float(input("Primeiro: "))
b = float(input("Segundo: "))
c = float(input("Teceiro: "))
d = float(input("Quarto: ")) 

lista = [a,b,c,d]
listaPosi = []
listaNeg = []

for i in lista:
    if i > 0:
        listaPosi.append(i)
    else: 
        listaNeg.append(i)

print("Positivos" +str(listaPosi))
tamanhoPosi = len(listaPosi)
print(tamanhoPosi)
print("Negativos" +str(listaNeg))
tamanhoNeg = len(listaNeg)
print(tamanhoNeg)
somaPosi = (sum(listaPosi))
somaNeg = (sum(listaNeg))

result1 = (somaPosi/tamanhoPosi)
print("Media positivos: " +str(result1))
result2 = (somaNeg/tamanhoNeg)
print("Media negativos: " +str(result2))
soma = (sum(lista))
print("Soma dos elementos: " +str(soma))