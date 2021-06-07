#Catetos e hipotenusa
co = float(input('Comprimento do cateto oposto:'))
ce = float(input('Comprimento do cateto adiacente:'))
hi = (co ** 2 + ce ** 2 ) ** (1/2)
print(' A hipotenusa vai medir {:.2f}'.format(hi))