else
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[ 1 ] converter para BANARIO
[ 2 ] canverter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} caonverter para BINARIO e igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} caonverter para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} caonverter para  e HEXADECIMAL igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opçao invalida Tente novamente')