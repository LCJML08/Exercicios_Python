'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
notas = []
aluno = []
turma = []
c = 0
r = '.'
while True:
    '''
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1,nota2],media])
    '''
    aluno.append(str(input('Nome: ')).strip().lower().capitalize())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    aluno.append(float((notas[0]+notas[1])/2))
    turma.append(aluno[:])
    aluno.clear()
    notas.clear()
    c += 1
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
    else:
        r = '.'
print('-='*40)
print(f'{"BOLETIM DOS ALUNOS":^80}')
print('-='*40)
print(f'{"N°":<4}',f'{"Nome":<15}',f'{"Média":<7}')
for y, x in enumerate(turma):
    print(f'{(y):<4}',f'{x[0]:<15}',f'{x[2]:<7.2f}')
while True:
    a = int(input('Mostrar nota de qual aluno [999 para finalizar]: '))
    if a == 999:
        break
    else:
        print(f'As notas de {turma[a][0]}, são: {turma[a][1]}')
print(f'{" PROGRAMA FINALIZADO ":=^50}')

