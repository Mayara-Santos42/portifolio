sexo = str(input("Digite seu sexo? [M/F]: ")).upper().strip()
while sexo not in "MmFf":
    sexo = str(input("INVÁLIDO! Digite novamente seu sexo? [M/F]: ")).upper()
print("Sexo {} registrado com sucesso!".format(sexo))
