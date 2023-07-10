# o programa deve converter as medidas de temperatura
c = float(input('Qual a temperatura em °C: '))
f = (c*9)/5 + 32
print('A temperatura {:.1f}°C, corresponde à {:.1f}°F'.format(c,f))
