lista = []
pares = []
impares = []
while True:
    r = '.'
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    while r not in 'SN':    
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')
