lista = []
pares = []
ímpares = []
while True:
    val = int(input("Digite um valor: "))
    if val not in lista:
        lista.append(val)
    resp = str(input("Deseja continuar? S/N: "))
    if resp in "Nn":
        break
for i, v in enumerate(lista):
    if v % 2 == 0 :
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)

print(f"A lista completa é {lista}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {ímpares}")