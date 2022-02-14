i = 0
n = 5
# j = 0
''' while i < n:
    while j < n:
        print(j)
        j += 1
    print(i)
    i += 1 '''

'''while i < n:
     j = 0
     while j < n:
         print(i , j)
         j += 1
     i += 1
# Vai repetir J, para cada valor de i '''

''' Dado um número N de empresas, e um número M de meses, e o ganho e gastos positivos e inteiro de cada empresa
para cada mês, imprimir se a empresa nesses meses ficou com déficit, lucro ou indiferente e imprimir o valor
correspondente a essa balança.'''

n = int(input("Digite o número de empresas: "))
m = int(input("Digite o número de meses: "))
empresa = 1
print("")
while empresa <= n:
    mes = 1
    balanca = 0
    print("Empresa {}. ".format(empresa))
    while mes <= m:
        print("Mês {}. ".format(mes))
        ganho = int(input("Digite o ganho da empresa no mês: "))
        gasto = int(input("Digite o gasto da empresa no mesmo mês: "))
        balanca += (ganho - gasto)
        print("")
        mes += 1
    if balanca == 0:
        print("A empresa {}, ficou indiferente (balança = R$ 0)".format(empresa))
    elif balanca > 0:
        print("A empresa {}, fechou com o lucro de R$ {}.".format(empresa, balanca))
    else:
        print("A empresa {}, fechou com o déficit de R$ {}.".format(empresa, balanca))
    empresa += 1
    print("\n")

