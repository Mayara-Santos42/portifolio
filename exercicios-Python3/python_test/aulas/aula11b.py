a = 3
b = 5
print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m.".format(a, b))

nome = "Mayara"
print("Olá muito prazer em te conhecer, {}{}{}!!!".format("\033[4;34m", nome , "\033[m"))
#Finalizar a estrutura!!

cores = {"Limpa":"\033[m" ,
          "azul":"\033[34m" ,
          "amarelo":"\033[33m" ,
          "pretoebranco":"\033[7;30m"}

print("Olá muito prazer em te conhecer, {}{}{}!!!".format(cores["pretoebranco"], nome, cores["Limpa"]))