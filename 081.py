c = e = 0
lista = []
while True:
    n = int(input('Digite um número: '))
    if c == 0 or n < lista[-1]:
        lista.append(n)
    else:
        e = 0
        while n < lista[e]:
            e += 1
        lista.insert(e,n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
    else:
        c += 1
#lista.sort(reverse=True)                                        OUTRA FORMA DE ORDENAR A LISTA
print(f'Você digitou {len(lista)} elementos')
print(f'Em ordem decrescente eles ficam assim: {lista}')
print('O valor 5 faz parte da lista!' if 5 in lista else 'O valor 5 não faz parte da lista!')
