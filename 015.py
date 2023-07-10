# O programa deve calcular o custo de aluguel de um carro
dias = int(input('Digite quantos dias o carro foi alugado: '))
km = float(input('Digite quantos km foram rodados com o carro nesse período: '))
aluguel = (dias*60) + (km*0.15)
print('O aluguel do carro é de R${:.2f}'.format(aluguel))
