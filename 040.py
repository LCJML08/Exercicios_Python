'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida'''
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('O aluno teve média de {:.2f} pontos \nPor isso, está {}REPROVADO{}'.format(m,'\033[1;34m','\033[m'))
elif m >= 5 and m < 7:
    print('O aluno teve média de {:.2f} pontos \nPor isso, está de {}RECUPERAÇÃO{}'.format(m,'\033[1;34m','\033[m'))
else:
    print('O aluno teve média de {:.2f} pontos \nPor isso, está {}APROVADO{}'.format(m,'\033[1;34m','\033[m'))
    