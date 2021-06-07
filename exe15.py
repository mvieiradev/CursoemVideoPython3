dias = int(input('Quantos dias alugado?'))
Km = float(input('Quantos Km rodados?'))
pago = (dias * 60) + (Km * 0.15)
print('O total a pagar e de R${:.2f}'.format(pago))



