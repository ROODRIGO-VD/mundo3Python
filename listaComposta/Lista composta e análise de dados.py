temp = []
princ = []

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Deseja continuar? S/N? "))
    if resp in "Nn":
        break

print(f"Os dados foram {princ}")