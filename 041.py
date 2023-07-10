'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade:

 Até 9 anos: MIRIM

 Até 14 anos: INFANTIL

 Até 19 anos: JÚNIOR

 Até 25 anos: SÊNIOR

 Acima de 25 anos: MASTER'''
from datetime import date
nascimento = int(input('Ano de Nascimento: '))
ano = date.today().year
idade = ano - nascimento
print('O atleta tem {}{}{} anos de idade'.format('\033[1;34m',idade,'\033[m'))
if idade <= 9:
    print('Está na categoria {}MIRIM{}'.format('\033[1;34m','\033[m'))
elif idade > 9 and idade <= 14:
    print('Está na categoria {}INFANTIL{}'.format('\033[1;34m','\033[m'))
elif idade > 14 and idade <= 19:
    print('Está na categoria {}JÚNIOR{}'.format('\033[1;34m','\033[m'))
elif idade > 19 and idade <= 25:
    print('Está na categoria {}SÊNIOR{}'.format('\033[1;34m','\033[m'))
else:
    print('Está na categoria {}MASTER{}'.format('\033[1;34m','\033[m'))
    