# o programa deve agir com um radar de trânsito
v = int(input('Qual é a velocidade do carro em KM: '))
if v <= 80:
    print('Você está dentro do limite!')
else:
    m = float((v-80) * 7)
    print('Você ultrapassou o limite de velocidade! Sua multa é de R${:.2f}'.format(m))
    