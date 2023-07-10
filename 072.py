'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
a = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = int(input('Escreva um número de 0 à 20: '))
while 20 < n or n < 0:
    n = int(input('Tente novamente. Escreva um número de 0 à 20: '))
print(f'Você escreveu o número {a[n]}')
