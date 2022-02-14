from math import pow , sqrt
print("Calcule e mostre o comprimento da Hipotenusa!")

catop = float(input("CATETO OPOSTO: "))
catad = float(input("CATETO ADJACENTE: "))
hip = pow(catop, 2) + pow(catad, 2)

total = sqrt(hip)

print("CATETO OPOSTO:{} ; CATETO ADJACENTE: {} ; HIPOTENUSA: √ {}.".format(catop, catad, hip))
print("O valor da HIPOTENUSA É: {:.3f}.".format(total))
