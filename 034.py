'''Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
s = float(input('Qual o salário do funcionário: R$'))
a = s + (s/100)*15 if s <= 1250 else s + (s/100)*10
print('Com um aumento proporcional, o salário passa a ser de R${:.2f}'.format(a))
