fr = str(input("Digite uma frase:")).upper()

print("Quantas vezes aparece a letra A? {}.".format(fr.count("A")))

print("Em que posição ela aparece a primeira vez? {}. \n E a última vez? {}.".format(fr.find("A")+1 , fr.rfind("A")+1))