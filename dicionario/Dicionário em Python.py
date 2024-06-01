aluno = {}
aluno["Nome"] = input("Nome: ")
aluno["Média"] = float(input("Média: "))
for v, k in aluno.items():
    print(f"- {v} é {k}")
if aluno["Média"] >= 7.0:
    print("- situação igual a Aprovado")
elif aluno["Média"] < 7:
    print("- situação igual a Recuperação")