num = int(input('digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analizando o numero {}'.format(num))
print('O numero {} tem {} unidades'.format(num, u))
print('O numero {} tem {} dezenas'.format(num, d))
print('O numero {} tem {} centenas'.format(num, c))
print('O numero {} tem {} milhares'.format(num, m))
