c = float(input("Informe a temperatura em °C: "))
k = c + 273
k = float(input("Informe a temperatura em K: "))
c = k - 273

c = float(input("Informe a temperatura em °C: "))
f = (1.8 * c) + 32
f = float(input("Informe a temperatura em °F: "))
c = (f - 32) / 1.8

f = float(input("Informe a temperatura em °F: "))
k = (f - 32 ) / 1.8 + 273
k = float(input("Informe a temperatura em K: "))
f = (k - 273) * 1.8 + 32


print("A temperatura de {}°C, corresponde a {}K.".format(c , k ))
print("A temperatura de {}K, corresponde a {}°C".format(k , c))

print("A temperatura de {}°C, corresponde a {}°F.".format(c ,f ))
print("A temperatura de {}°F, corresponde a {}°C.".format(f , c))

print("A temperatura em {}°F, corresponde a {}K.".format( f , k))
print("A temperatura de {}K, corresponde a {}°F.".format(k , f))

