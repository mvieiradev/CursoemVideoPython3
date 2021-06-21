#Alistamento Militar
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    soldo = 18 - idade
    print('Ainda faltam {} para o alistamento'.format(soldo))
    ano = atual + soldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    soldo = 18 - idade
    print('voce deveria ter se alistado ha {} anos '.format(soldo))
    ano = atual - soldo
    print('Seu alistamento foi em {}'.format(ano))