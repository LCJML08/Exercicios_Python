'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

 à vista dinheiro/cheque: 10% de desconto

 à vista no cartão: 5% de desconto

 em até 2x no cartão: preço formal 

 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' {}TUDO CONVENIÊNCIA{} '.format('\033[1;34m','\033[m')))
v = float(input('Digite o valor do produto: R$'))
print('--- {}FORMAS DE PAGAMENTO{} ---'.format('\033[1;34m','\033[m'))
print('{}(1){} - À vista com dinheiro ou cheque'.format('\033[1;34m','\033[m'))
print('{}(2){} - À vista no cartão'.format('\033[1;34m','\033[m'))
print('{}(3){} - 2x no cartão'.format('\033[1;34m','\033[m'))
print('{}(4){} - 3x ou mais no cartão'.format('\033[1;34m','\033[m'))
o = int(input('Selecione a sua opção: '))
if o == 1:
    print('O valor do produto sairá por R${:.2f}, com desconto de 10%'.format(v-(v/100)*10))
elif o == 2:
    print('O valor do produto sairá por R${:.2f}, com desconto de 5%'.format(v-(v/100)*5))
elif o == 3:
    print('O valor sairá pelo preço nomal de R${:.2f}'.format(v))
elif o == 4:
    p = int(input('Digite quantas parcelas serão: '))
    v = v+(v/100)*20
    print('As parcelas terão valor de R${:.2f}'.format(v/p))
    print('O valor total do produto sairá por R${:.2f}, com juros de 20%'.format(v))
else:
    print('Essa função não existe')
