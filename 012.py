# O programa deve mostrar o valor do produto com desconto de 5%
valor = float(input('Qual o valor do produto? R$'))
desconto = valor - (valor/100)*5
print('O produto que custa R${:.2f}, com desconto de 5%, vai sair por R${:.2f}'.format(valor,desconto))
