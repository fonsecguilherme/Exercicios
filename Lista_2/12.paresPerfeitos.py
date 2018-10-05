listaDeNumeros = []
listaDeNumeros2 = []
listaFinal = []
num = 1
i = 0

while i < 500:
    if (i * 2) + 1 == num:
        listaDeNumeros.append(i)
        listaDeNumeros2.append(num)
        listaFinal = listaDeNumeros + listaDeNumeros2
    num += num
    
print("Pares correspondentes: " +str(listaFinal))