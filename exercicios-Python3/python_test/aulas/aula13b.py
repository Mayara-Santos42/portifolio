n = int(input("Digite um número: "))
for c in range(0 , n+1):
    print(c)
print("Fim")

#Parte de passagem para FOR!]

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i , f+1 , p):
    print(c)
print("Fim")

for c in range(0 ,3):
    b = int(input("Digite um valor: "))
print("FIM")

s = 0
for c in range(0, 2):
    n = int(input("Digite um valor: "))
    s += n
print("Somatório: {}.".format(s))