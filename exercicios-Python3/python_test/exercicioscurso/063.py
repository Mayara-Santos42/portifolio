print("SEQUÊNCIA FIBONACCI!")
print("------"*15)
n = int(input("Quantos termos você deseja mostrar? "))
termo1 = 0
termo2 = 1
print("{} - {} - ".format(termo1, termo2), end='')
cont = 3
while cont <= n:
    termo3 = termo1 + termo2
    print("- {}".format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print("- FIM")
