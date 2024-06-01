m = int(input("Número de linhas: "))
n = int(input("Número de colunas: "))
matriz = []
for linha in range(m):
    linha = []
    for coluna in range(n):
        elemento = input(f"Elemento da linha {linha} e coluna {coluna}")
        linha.append(float(elemento))
    matriz.append((linha))