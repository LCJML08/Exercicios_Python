exp = str(input('Digite a sua expressão: '))
abre = []
fecha = []
for p, c in enumerate(exp):
    if c in '(':
        abre.append(c)
    elif c in ')':
        fecha.append(c)
if len(abre) == len(fecha):
    print('Sua expressão está válida!')
else:
    print('Sua expressão não é válida!') 
    