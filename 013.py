# O programa deve mostrar o reajuste de 15% do salário do empregado
s = float(input('Quanto é o salário? R$'))
a = s + (s/100)*15
print('O funcionário que antes recebia R${:.2f}, com o reajuste de 15%, vai passar a receber R${:.2f}'.format(s,a))
