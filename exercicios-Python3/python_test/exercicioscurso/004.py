a = input('Digite algo:')
print('O tipo primitivo desse valor é ',type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Possui letras minúsculas?', a.islower())
print('Possui letras maiúsculas?', a.isupper())
print('Está capitalizada?', a.istitle())