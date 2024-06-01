numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite outro valor: "))
numero3 = int(input("Digite mais um valor: "))
numero4 = int(input("Digite o último valor: "))

numeros = (numero1, numero2, numero3, numero4)
a = numeros.count(9)
print(f"Aqui está sua lista: {numeros}")
#Quantos 9 há na tupla
if 2 <= a <= 4:
    print(f"O valor 9 apareceu {a} vezes.")
elif a == 1:
    print(f"O valor 9 apareceu {a} vez.")
elif a == 0:
    print("O valor 9 não apareceu.")
#Posição do número 3 na tupla
if 3 in numeros:
    print(f"O número 3 está na posição {numeros.index(3) + 1 }")
elif 3 not in numeros:
    print("Sua lista não contém o número 3")
#Números pares na tupla
print("Os valores pares digitados foram:  ", end="")
for n in numeros:
    if n % 2 == 0:
        print(n, end=" | ")