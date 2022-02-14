"""Peça para o usuário entrar com o ínicio e o fim da tabuada
e imprima a tabuada correspondente dentro dos intervalos considerados:
EX:
Começo = 1
Fim = 2
--------------------------------------
Para o 1:
1x1 = 1
1x2 = 2
1x3 = 3
Para o 2:
2x1 = 2
2x2 = 4
2x3 = 6"""

inicio = int(input("Começo = "))
fim = int(input("Fim = "))
for i in range(inicio , fim+1 ):
    print("Para o", i)
    for j in range(inicio, fim+1):
        print("{}x{} = {}". format(i , j , i * j))

        print("")


