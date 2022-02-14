p = float(input('Preço do produto:'))
desc = p*0.05
f = p-desc
print('Preço do seu produto {}; 5% de desconto= {}.'.format(p, desc))
print('Valor final= {}'.format(f))