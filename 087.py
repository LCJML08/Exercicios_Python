matriz = [[],[],[]]
pares = maior = tc = sl = 0
for l in range (0,3):
    for c in range (0,3):
        matriz[l].append(int(input(f'Digite um número para a posição ({l},{c}): ')))
'''
print(f'[ {} ] [ {} ] [ {} ] 
      [ {} ] [ {} ] [ {} ] 
      [ {} ] [ {} ] [ {} ]')
'''
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=(' '))
    print()
for p, li in enumerate(matriz):
    for co in range(0,3):
        if li[co] % 2 == 0:
            pares += li[co]
        if co == 2:
            tc += li[co]
        if p == 0 and co == 0:
            maior = li[co]
        elif p == 1:
            if maior < li[co]:
                maior = li[co]
print(f'A soma de números pares é {pares}')
print(f'A soma dos valores da terceira coluna é {tc}')
print(f'O maior valor da segunda linha é {maior}')
