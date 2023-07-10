'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

c = 0
times = ('Bota Fogo','Grêmio','Flamengo','Palmeiras','Bragantino','Fluminense','São Paulo','Internacional','Athletico-PR','Atlético-MG','Fortaleza','Cruzeiro','Cuiabá','Santos','Bahia','Corinthias','Goiás','Vasco da Gama','América-MG','Coritiba')
print('-'*50)
print(f'Lista de times: {times}')
print('-'*50)
print(f'Os cincos primeiro times da Tabela do Brasileirão são {times[:5]}')
print('-'*50)
print(f'Os últimos 4 colocados são {times[-4:]}')
print('-'*50)
print(f'A lista em ordem alfabética fica: {sorted(times)}')
print('-'*50)
'''while True:
    if times[c] == 'Fluminense':
        print(f'O Fluminense está na {c+1}° posição')
        break
    else:
        c +=1'''
print(f'O Fluminense está na {times.index("Fluminense") + 1}ª posição')
        