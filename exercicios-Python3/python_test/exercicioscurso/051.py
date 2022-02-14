number = int(input("Digite o 1° termo da sua Progressão Aritimética: "))
razao = int(input("Agora digite a sua razão: "))
decimoTermo = number + 9 * razao
for c in range(number , decimoTermo , razao):
    print(c)

#refazer