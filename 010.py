# O programa deve converter a moeda
real = float(input('Quanto dinheiro você tem? R$'))
dolar = real/4.76
print('Com R${:.2f}, você pode comprar U${:.2f}'.format(real,dolar))
