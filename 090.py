boletim = {}
boletim['Nome'] = str(input('Nome do Aluno: ')).strip().lower().capitalize()
boletim['Média'] = float(input('Média do Aluno: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Reprovado'
print(f'Nome do Aluno: {boletim["Nome"]}')
print(f'Média do Aluno: {boletim["Média"]}')
print(f'Situação do Aluno: {boletim["Situação"]}')
