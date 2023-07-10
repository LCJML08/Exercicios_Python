# O programa deve mostrar as relações da string escrita
nome = str(input('Digite seu nome: ')).strip()
separado = nome.split()
print('Seu nome em Maiúsculas fica: {}'.format(nome.upper()))
print('Seu nome em Minúsculas fica: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(separado[0], len(separado[0])))
