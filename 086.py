lista = [[],[]]
for c in range (1,8):
    n = (int(input(f'Digite o {c}° número: ')))
    if (n%2) == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Lista de números pares digitados: {lista[0]}')
print(f'Lista de números ímpares digitados: {lista[1]}')
