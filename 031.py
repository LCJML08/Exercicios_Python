# O programa deve calcular o preço da passagem (R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas)
km = int(input('Qual a distância da viagem em KM: '))
p = float(km *0.5 if km <= 200 else km * 0.45)
print('O preço da viagem é R${:.2f}'.format(p))
