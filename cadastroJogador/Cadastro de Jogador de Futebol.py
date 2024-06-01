dados = {}
partidas = []
dados["nome"] = str(input("Nome do Jogador: "))
total = int(input(f"Quantas partidas {dados["nome"]} jogou ? "))
for gols in range(1, total+1):
    partidas.append(int(input(f"Quantos gols na partida {gols}? ")))

dados["total"] = sum(partidas)
dados["gols"] = partidas[:]
print("-=" * 30)
print(dados)
print("-=" * 30)

for v, k in dados.items():
    print(f"O campo {v} tem o valor {k}")
print("-=" * 30)
print(f"O jogador {dados["nome"]} jogou {dados["total"]} partidas")
for i, v in enumerate(dados["gols"]):
    print(f"    => Na partida {i}, fez {v} gols")
print(f"Foi um total de {dados["total"]} gols")