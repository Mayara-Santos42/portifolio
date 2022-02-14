n = int(input("Digite o 1° termo da sua PA: "))
r = int(input("Agora digite a sua razão: "))
dec = n
cont = 1
total = 0
maisTermo = 10
# O primeiro ele passa a valer 10
while maisTermo != 0:
    total = total + maisTermo
    while cont <= total:
        print("{} - ".format(dec), end='')
        dec += r
        cont += 1
    print("Pausa...")
    maisTermo = int(input("Você deseja mostrar mais quantos termos? "))
print("Progressão finalizada com {} termos.".format(total))