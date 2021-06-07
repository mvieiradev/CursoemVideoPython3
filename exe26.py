#Primeira e ultima ocorrencia de uma string
frase =  str(input('Digite ua Frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase: '.format(frase.count('A')))
print('A primeira letra A aparece na posiçao {}'.format(frase.find('A')+1))
print('A ultima letra A aprece na posiçao {}'.format(frase.rfind('A')+1))
