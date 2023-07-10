# O programa deve mostrar a hipotenusa de um triângulo
from math import hypot, trunc
ca = float(input('Digite o valor do Cateto Adjacente do Triângulo: '))
co = float(input('Digite o valor do Cateto Oposto do Triângulo: '))
h = trunc(hypot(ca,co))
print('O valor da Hipotenusa do Triângulo é: {}'.format(h))
