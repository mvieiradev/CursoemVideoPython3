#Analisandor de texto
nome = str(input('digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('seu nome em amiuscolas e {}'.format(nome.upper()))
print('seu nome em minuscolas e {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print(' Seu primeiro no e {} e ele tem {} letras'.format(separa[0], len(separa[0])))
