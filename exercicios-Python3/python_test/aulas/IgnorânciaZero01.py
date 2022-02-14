for c in range(10 , 0, -1):
    print(c)

n = 10
for cont in range(n):
    print(cont+1)

for i in range(2, 6 , 2):
    print(i)

# x = int(input("Digite o valor de x: "))
# fatorial = 1
# for fator in range(2, x+1):
    #fatorial *= fator
   # print(fatorial)

x = int(input("Digite o valor de X: "))
fatorial = 1
for fator in range(x, 1 , -1): #Decrementando o valor da sequência.
    fatorial *= fator
print("O valor de {}!, é igual a {}.".format(x, fatorial))




