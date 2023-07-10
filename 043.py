'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

 IMC abaixo de 18,5: Abaixo do Peso

 Entre 18,5 e 25: Peso Ideal

 25 até 30: Sobrepeso

 30 até 40: Obesidade

 Acima de 40: Obesidade Mórbida'''
p = float(input('Digite o peso em Kg: '))
a = float(input('Digite a altura em Metros: '))
imc = p / (a**2)
print('O IMC é: {}{:.1f}{}'.format('\033[;34m',imc,'\033[m'))
if imc < 18.5:
    print('Status: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Satus: PESO IDEAL')
elif 25 <= imc < 30:
    print('Status: SOBREPESO')
elif 30 <= imc <= 40:
    print('Status: OBESIDADE')
else:
    print('Satus: OBESIDADE MÓRBIDA')
    