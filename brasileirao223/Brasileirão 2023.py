times = ("Botafogo", "Bragantino", "Flamengo", "Palmeiras", "Athletico-PR", "Grêmio", "Atlético-MG", "Fortaleza"
         , "Fluminense", "São Paulo", "Cuiabá", "Internacional", "Bahia", "Cruzeiro", "Corinthians", "Goiás", "Vasco", "Santos", "Coritiba", "América-MG")


def p():
    print("=-"*15)


p()
print(f"Lista de times do Brasileirão 2023: {times}")
p()
print(f"Os cinco primeiros da Tabela são: {times[0:5]}")
p()
print(f"Os quatro últimos da Tabela são: {times[16:]}")
p()
print(f"A tabela em ordem alfabética é: {sorted(times)}")
p()
print(f"O São Paulo está em {times.index("São Paulo") + 1} lugar")
