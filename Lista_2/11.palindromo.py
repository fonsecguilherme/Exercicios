num = (input("Digite o número a ser verificado: "))

nvNum = num[::-1]

if nvNum == num: 
    print("Palindromo")
else: 
    print("Não é palindromo")