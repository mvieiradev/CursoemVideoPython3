#Reajustando Descontos
salario = float(input('Qual e o salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionatio que ganhava R${}, com 15% de aumento, passa a receber R${}'.format(salario, novo))