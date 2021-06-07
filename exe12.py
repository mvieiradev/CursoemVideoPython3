preço = float(input('Qual e o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
#print('O produto que custava R${}, na promoçao com deconto de 5% vai custar R${}'.format(preço, novo))
print(f'O produto que custava R${preço}, na promoçao com deconto de 5% vai custar R${novo}')