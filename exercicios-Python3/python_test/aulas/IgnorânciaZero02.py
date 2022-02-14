"""Um número triângular é calculado pela fórmula triangular = n * (n + 1) / 2
Sendo n o índice desse número tringular
Escreva um programa que imprima os números trianguares com índices múltiplos de 5 entre 5 e 50."""

""" EXEMPLO:
primeiroTri = 1
segundoTri= 3"""


for n in range(5, 51, 5):
    triangular = n * (n + 1) // 2
    print("{} número triangular = {}.".format(n ,triangular))
