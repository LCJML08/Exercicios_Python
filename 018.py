# O programa deve mostrar o Seno, o Cosseno e a Tagente de um grau digitado
from math import sin, cos, tan, radians
g = float(input('Digite o valor do Grau que você quer consultar: '))
r = radians(g)
s = sin(r)
c = cos(r)
t = tan(r)
print(' O Seno vale: {:.2f} \n O Cosseno vale: {:.2f} \n E a Tangene vale: {:.2f}'.format(s,c,t))
