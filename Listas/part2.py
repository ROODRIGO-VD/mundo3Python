galera = []

for c in range(0, 2):
    nome = str(input("Qual seu nome? "))
    idade = int(input("Qual sua idade: "))
    dado = [nome, idade]
    galera.append(dado)

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
    else:
        print(f"{p[0]} é menor de idade.")
