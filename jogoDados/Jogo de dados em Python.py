from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    "Jogador 1": randint(1, 6),
    "Jogador 2": randint(1, 6),
    "Jogador 3": randint(1, 6),
    "Jogador 4": randint(1, 6),
}
ranking = []
print("Valores sorteados:")
for v, k in jogo.items():
    sleep(0.6)
    print(f"O jogador {v} tirou {k} no dado.")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("-=" * 30)
print("== RANKING DOS JOGADORES == ")
for i, v in enumerate(ranking):
    print(f"O {i + 1} lugar: {v[0]} com {v[1]} pontos.")
