# Ciclos
#condição continuou sempre verdadeira!
'''n = 10
 cont = 0
while cont < n:
   print(cont) '''

'''n = 10
cont = 0
while cont < n:
    print(cont)
    cont +=1'''

''' base = int(input("Digite o valor da base: "))
expo = int(input("Digite o valor do expoente: "))
cont = 0
prod = 1
# A variável CONT se inicia com 0, então se o EXPO > CONT ele vai realizar o nosso laço
# no entanto, a recíproca também é verdadeira, pois se CONT < EXPO o ciclo vai continuar
while expo > cont:
    prod = prod * base
    cont += 1
print("{} elevado a {} é igual {}.".format(base,expo, prod)) '''

''' num = int(input("Digite um número para descobrir o seu fatorial: "))
prod = num
#O valor do meu prod deve ser ele mesmo p/ decrementa-lo
cont = num - 1
fatorial = 1
while cont > 1:
    prod = prod * cont
    cont -= 1
# Até chegar no número 1, ele para o ciclo
print("{}! é igual {}.".format(num, prod)) '''

''' n = int(input("Digite um número para descobrir o seu fatorial: "))
prod = 1
cont = 2
while cont <= n:
    prod = prod * cont
    cont += 1
print("{}! é igual {}.".format(n, prod)) '''

n = int(input("Digite o primeiro número: "))
while n != 0:
    print(n , "² =", n*n)
    n = int(input("Digite o próximo número: "))
