lista = [[], []]

for num in range(1, 7+1):
    numeros = int(input(f"Digite o {num}o. valor: "))
    if numeros % 2 == 0:
        lista[0].append(numeros)
    elif numeros % 2 == 1:
        lista[1].append(numeros)

print(f"Os valores pares digitados foram: {sorted(lista[0])}")
print(f"Os valores ímpares digitados foram: {sorted(lista[1])}")