# o programa mostra qual é o número maior e o menos dentre 3 escolhidos
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior número digitado foi: {} \nO menor número digitado foi: {}'.format(maior,menor))
