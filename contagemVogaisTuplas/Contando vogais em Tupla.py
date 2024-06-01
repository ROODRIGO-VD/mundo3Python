palavras = ("APRENDER",
            "PROGRAMAR",
            "LINGUAGEM",
            "CURSO",
            "GRATIS",
            "ESTUDAR",
            "PRATICAR",
            "TRABALHAR",
            "MERCADO",
            "PROGRAMADOR",
            "FUTURO")


for n in palavras:
    print(f"\nNa palavra {n} temos ", end="")
    for l in n:
        if l in "AEIOU":
            print(l, end=" ")


