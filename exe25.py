#Procurando uma string dentro de outra
nome = str(input('Qal o seu nome')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))