galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Nome: "))
    while True:
        pessoa["sexo"] = str(input("[M/F]: ")).upper()
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Por favor, digite M ou F")
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        continuar = str(input("Deseja continuar? [S/N]")).upper()
        if continuar in "SN":
            break
        print("Responda apenas S ou N")
    if continuar == "N":
        break
print("-=" * 30)
print(f"A) Ao todo temos {len(galera)} cadastradas")
media = soma / len(galera)
print(f"B) A média das idades é de {media}")
print(f"As mulheres cadastradas foram ", end="|")
for p in galera:
    if p["sexo"] in "F":
        print(f"{p["nome"]}", end="| ")

