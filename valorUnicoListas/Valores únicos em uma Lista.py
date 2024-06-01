lista = []

while True:
    val = int(input("Digite um valor: "))
    if val not in lista:
        lista.append(val)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar.")
    resp = str(input("Deseja continuar? S/N: "))
    if resp in "Nn":
        break
print(f"Lista Ordenada {sorted(lista)}")
