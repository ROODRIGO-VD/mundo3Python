lista = []
maior = 0
menor = 0
for cont in range(0,5):
    lista.append(int(input(f"Digite um valor para a Posição {cont}: ")))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print("=-"*30)
print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {maior}, esse valor está nas posições ", end="")
for c, v in enumerate(lista):
    if v == maior:
        print(f"{c}...", end="")
print()
print(f"O menor valor digitado foi {menor}, esse valor está nas posições ", end="")
for c, v in enumerate(lista):
    if v == menor:
        print(f"{c}...", end="")