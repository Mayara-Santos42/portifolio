nome = str(input("Qual é o seu nome?"))
if nome == "Mayara":
    print("Que nome bonito!")
elif nome == "Camila" or nome == "Maria" or nome == "Gabriele":
    print("Seu nome é muito comum no país!")
elif nome in "Ana Claudia Jéssica Juliana":
    #Criou uma lista, você pode programar para que seja maior.
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal!")
print("Tenha um bom diaaa, {}!!".format(nome))