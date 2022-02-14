numero = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão: 
[1] Binário
[2] OCTAL
[3] HEXADECIMAL""")
opcoes = int(input("Sua opção: "))
if opcoes == 1:
    print("{} convertido em BINÁRIO é igual a {}.".format(numero, bin(numero)[2:]))
elif opcoes == 2:
    print("{} convertido em OCTAL é igual a {}.".format(numero, oct(numero)[2:]))
elif opcoes == 3:
    print("{} convertido em HEXADECIMAL é igual a {}.".format(numero, hex(numero)[2:]))
else:
    print("Opção Inválida! TENTE NOVAMENTE!")
# fatiamento de str
