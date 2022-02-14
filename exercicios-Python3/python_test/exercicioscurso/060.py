print("Vamos calcular o fatorial!?")
numero = int(input("Digite um número: "))
cond = numero
fatorial = 1
while cond > 0:
    print("{} ".format(cond), end='')
    print("x " if cond > 1 else "= " , end='')
    fatorial = fatorial * cond
    cond -= 1
print(fatorial , end="")
print("\n"*1)
print("O fatorial de {}! é igual a {}.".format(numero, fatorial))