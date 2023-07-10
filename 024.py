# O programa deve apontar se o nome da cidade começa com a palavra "Santo"
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == "SANTO")
