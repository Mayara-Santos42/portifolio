import math
print("Calcule os repectivos SENO, COSSENO & TANGENTE do ângulo a seguir:")
ang = float(input("Digite um ângulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tag = math.tan(math.radians(ang))

print("O ângulo é {}. Apresente SENO {:.3f}, COSSENO {:.3f} & TANGENTE {:.3f}.".format(ang, sen, cos, tag))