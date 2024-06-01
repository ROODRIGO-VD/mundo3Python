#Tecnicas para acessar elementos de uma tupla

#TUPLA
lanche = ("Hamburguer","Suco","Pizza","Pudim")
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
#TECNICA 1
def lanche1(lanche):
    for cont in range(0, len(lanche)):
        print(f"Eu vou comer {lanche[cont]}")


#TECNICA 2
def lanche2(lanche):
    for comida in lanche:
        print(f"Eu vou comer {comida}")

#TECNICA 3 PARA SABER A POSICAO TAMBÉM
def lanche3(lanche):
    for cont in range(0, len(lanche)):
        print(f"Eu vou comer {lanche[cont]} na posição {cont}")

#TECNICA 3 PARA SABER A POSICAO TAMBÉM
def lanche4(lanche):
    for pos, comida in enumerate(lanche):
        print(f"Eu vou comer {comida} na posição {pos}")

#Juntar as Tuplas em Ordem crescente
def a_b_cresc(a,b):
    c = sorted(a+b)
    print(c)
#Juntas as Tuplas em Ordem decrescente
def a_b_decre(a,b):
    c = sorted(a + b,reverse=True)
    print(c)
#Usando Vários Métodos na junção das tuplas
def a_b_mult(a, b, c):
    print(f"A junção das tuplas A {a} e B {b} fornece um total de {len(c)} números ")
    print(f"O número 2 aparece {c.count(2)} vezes.")

