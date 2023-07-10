# o programa deve idetificar se existe "Silva" no nome
nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.upper()
print (-1 != nome.find("SILVA"))

'''
print ('Seu nome tem "Silva"? {}').format('SILVA' in nome.upper())
'''
