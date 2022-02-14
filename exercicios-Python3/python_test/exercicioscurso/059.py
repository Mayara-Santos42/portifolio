valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))
opcao = 0
while opcao != 5:
    print('''   --- MENU ---
        [1] SOMA
        [2] MULTIPLICAÇÃO
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA''')
    opcao = int(input("Qual é a sua opção? "))
    if opcao == 1:
        soma = valor1 + valor2
        print("A soma entre os número é {}.".format(soma))
    elif opcao == 2:
        mult = valor1 * valor2
        print("A multiplicação entre os números é igual {}.".format(mult))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
            print("O primeiro número é o maior.")
        elif valor2 > valor1:
            print("O segundo número é maior.")
        else:
            print("Eles são iguais! ")
    elif opcao == 4:
        print("Novos números!")
        valor1 = int(input("Digite um número: "))
        valor2 = int(input("Digite outro número: "))
    elif opcao == 5:
        print("Acabou!!!")
    else:
        print("Opção inválida! Tente novamente...")
    print("-------------" * 1)
print("Fim do programa! Volte sempre!")
