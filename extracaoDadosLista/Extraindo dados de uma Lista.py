lista = []

while True:
    val = int(input("Digite um valor: "))
    if val not in lista:
        lista.append(val)
    resp = str(input("Deseja continuar? S/N: "))
    if resp in "Nn":
        break

print(f" Você digitou {len(lista)} elementos.\n Os valores em ordem"
      f"decrescente são: {sorted(lista, reverse=True)}")
if 5 in lista:
    print(" O valor 5 está na lista.")
else:
    print(" O valor 5 não foi encontrado na lista.")