#Jogo Adivinhaçao v.1.0
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5 tente adivinher...')
print('-=-' * 20)
jogador = int(input('em que numero eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS!voce consegui me vencer!')
else:
    print('GANHEI! eu pensei no numero {} e nao no {}'.format(computador, jogador))