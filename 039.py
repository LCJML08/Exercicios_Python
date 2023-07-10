'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
ano_nascimento = int(input('{}Digite o ano do seu nascimento:{} '.format('\033[1;34m','\033[m')))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print('Quem nasceu em {}, esse ano terá {} anos de idade'.format(ano_nascimento,idade))
if idade < 18:
    print('Ainda faltam {} anos para o seu alistamento militar que será em {}'.format(18 - idade, ano_nascimento + 18))
elif idade > 18:
    print('O período do seu alistamento militar foi há {} anos atrás, em {}'.format(idade - 18, ano_nascimento + 18))
else:
    print('O seu Alistamento militar será {}ESSE ANO{}, fique atento!'.format('\033[1;34m','\033[m'))
