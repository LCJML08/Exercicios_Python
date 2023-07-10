'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto o comprador recebe de renda mensal? R$'))
anos = int(input('Em quanto anos o comprador quer quitar a compra? '))
meses = anos * 12
prestacao = casa / meses
porcao = (salario / 100) * 30
if prestacao <= porcao:
    print('Para comprar a casa que custa R${:.2f}, em um período de {} ano(s), a prestação será de R${:.2f}'.format(casa,anos,prestacao))
    print('{}Financiamento Aprovado{}'.format('\033[4;33m','\033[m'))
else:
    print('Para comprar a casa que custa R${:.2f}, em um período de {} ano(s), a prestação será de R${:.2f}'.format(casa,anos,prestacao))
    print('{}Financiamento Negado{}'.format('\033[4;34m','\033[m'))
    