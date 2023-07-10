# O programa mostra se o ano é bissexto
from datetime import date
ano = int(input('Qual o ano a ser analisado (Coloque 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year
print('Este ano ({}) é Bissexto'.format(ano) if (ano%4) == 0 and (ano%100) != 0 or (ano%400) == 0 else 'Este ano ({}) não é Bissexto'.format(ano))
