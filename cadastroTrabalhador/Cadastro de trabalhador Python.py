from datetime import date
dados = {}
dados["nome"] = input("Nome: ")
nasc = int(input("Ano de nascimento: "))
dados["idade"] = date.today().year - nasc
dados["ctps"] = int(input("Carteira de trabalho (0 não tem):  "))
if dados["ctps"] != 0:
    dados["contratação"] = int(input("Ano de contratação: "))
    dados["salário"] = float(input("Salário: R$"))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - date.today().year)
print("-=" * 30)
for v, k in dados.items():
        print(f"- {v} tem o valor {k} ")

print("OU")

if dados["ctps"] == 0:
    print(f" Olá {dados["nome"]}, você possui {dados["idade"]} anos e você não possui carteira de trabalho")
elif dados["ctps"] != 0:
    print(f" Olá {dados["nome"]}, você possui {dados["idade"]} anos, sua carteira de trabalho é {dados["ctps"]},"
          f"você foi contratado no ano {dados["contratação"]}, com um salário de R${dados["salário"]:.2f}."
          f" Logo você irá se aposentar com {dados["aposentadoria"]}.")