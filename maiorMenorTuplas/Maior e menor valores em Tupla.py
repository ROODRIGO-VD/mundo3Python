from random import randint as r

numeros = (r(1, 10), r(1, 10), r(1, 10), r(1, 10), r(1, 10))

print("Os números sorteados foram: ", end="")
for n in numeros:
    print(n, end=" ")
print()
print(f"\nO maior número sorteado foi o {max(numeros)}")
print(f"O menor número sorteador foi o {min(numeros)}")