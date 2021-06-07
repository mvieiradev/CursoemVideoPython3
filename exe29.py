velocidade = float(input('qual a velocidade que o carro esta andando?'))
if velocidade > 80:
    print('MULTADO! Voce ultrapasol o limite permitido que e 80Km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagat uma multa de R${}!'.format(multa))
print('tenha um bom dia! Dirija com sigurança')