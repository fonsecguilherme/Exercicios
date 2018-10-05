num = int(input("Digite o número para verificação: "))

a = 0
b = 1
c = 2
d = 0

while d < num:
    a += 1
    b += 1
    c += 1
    d = a*b*c
if d == num:
    print("É triangular")
else:
    print("Não é triangular")
