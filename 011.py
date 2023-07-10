# O progama deve mostrar quantos litros de tinta precisa para a área quadrada da parede
# Se utiliza um litro de tinta para cada 2 metros quadrados
largura = float(input('Largura da Parede: '))
altura = float(input('Altura da parede: '))
area = float(largura*altura)
tinta = area/2
print('A dimensão da sua parede é de {} x {}, o que corresponde à uma área de {:.2f}m2. \n Serão necessários {:.0f}l de tinta para pintá-la'.format(largura,altura,area,tinta))
