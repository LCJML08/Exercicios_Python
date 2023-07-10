# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
f = str(input('Digite um frase: ')).strip()
f = f.upper()
print('A letra "A" apareceu {} vezes na frase!'.format(f.count("A")))
print('A primeira letra "A" está na posição {}'.format(f.find("A") +1))
print('E a última letra "A" está na posição {}'.format(f.rfind("A") + 1))
