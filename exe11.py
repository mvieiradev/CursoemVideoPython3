larg = float(input('Largura da parede'))
alt = float(input('Altura da parede'))
area = larg * alt
print('Sua parede tem a dimençao de {}x{} e seu area e de  {}m²:'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede ,voce presisara de {}l de tinta'.format(tinta))