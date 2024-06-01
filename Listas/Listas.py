lista = []


for cont in range(1, 6+1):
    lista.append(int(input(f"Digite um o {cont}° valor: ")))

for c, v in enumerate(lista):
    print(f"O número {v} está na posição {c}°")
