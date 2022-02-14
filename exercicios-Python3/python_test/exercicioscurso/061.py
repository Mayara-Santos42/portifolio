
'''number = int(input("Digite o 1° termo da sua Progressão Aritimética: "))
razao = int(input("Agora digite a sua razão: "))
decimoTermo = number + 9 * razao
for c in range(number , decimoTermo , razao):
    print(c)'''

n = int(input("Digite o 1° termo da sua PA: "))
r = int(input("Agora digite a sua razão: "))
dec = n
cont = 1
while cont <= 10:
    print("{} - ".format(dec), end='')
    dec += r
    cont += 1
print("\n FIM")