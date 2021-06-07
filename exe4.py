#Dissecando uma variavel
a = input('Digite algo: ')
print('O tipo primitivo desse valor e ', type(a))
print('Só tem espaço?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Esta em maiuscula?', a.isupper())
print('Esta em minusculas?', a.islower())
