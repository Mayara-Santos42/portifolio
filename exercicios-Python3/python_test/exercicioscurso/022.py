nome = str(input("Seu nome completo? "))
print("Todas as letras maiúsculas: {}.".format(nome.upper()))
print("Todas as letras minúsculas: {}.".format((nome.lower())))
espacos = nome.count("")
indice = len(nome)
print("Quantidade de letras: {}.".format(espacos, indice))
dividido = nome.strip()
print("Quantidade de letras do seu primeiro nome: {}.".format(len(dividido)))

dividido=nome.split()
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))