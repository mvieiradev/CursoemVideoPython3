#Custo de Viagen
distancia = float(input('Quale a distancia da sua viagem?'))
print('Voce esta prestes a comecar uma viagen de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem sera de R${:.2f}'.format(preço))