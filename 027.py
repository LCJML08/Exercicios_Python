# O programa deve mostrar o primeiro e o último nome da pessoa
nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.lower()
nome = nome.title()
nome = nome.split()
print('Prazer em te conhecer! \nSeu primeiro nome é {} \nE o seu último nome é {}'.format(nome[0],nome[-1]))
