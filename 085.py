pessoas = []
p = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')).strip().lower().capitalize())
    pessoas.append(float(input('Peso: ')))
    if len(p) == 0:
        maior = menor = pessoas[1]
    else:
        if menor > pessoas[1]:
            menor = pessoas[1]
        if maior < pessoas[1]:
            maior = pessoas[1]
    p.append(pessoas[:])
    pessoas.clear()
    r = '.'
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('='*50)
print(f'Foram cadastradas {len(p)} pessoas!')
print(f'O maior peso é {maior}KG de', end=(' '))
for c in p:
    if c[1] == maior:
        print(f'[{c[0]}] ')
print(f'O menor peso é {menor}KG de', end=(' '))
for c in p:
    if c[1] == menor:
        print(f'[{c[0]}] ')

'''
maior = []
menor = []
for y, x in enumerate(p):
    if y == 0:
        menor.append(x[:])
        maior.append(x[:])
    else:
        if menor[0][1] > x[1]:                                 #OUTRA FORMA QUE CADASTRA APENAS UM NOME POR PESO
            menor[0] = x[:] 
        if maior[0][1] < x[1]:
            maior[0] = x[:]
print(f'Forama cadastradas {len(p)} pessoas!')
print(f'O maior peso é {maior[0][1]:.1f}KG de {maior[0][0]}')
print(f'O menor peso é {menor[0][1]:.1f}KG de {menor[0][0]}')
'''
