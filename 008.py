#O programa deve mostrar as variações de medida do valor digitado em metros
m = float(input('Digite uma medida em metros: '))
km = m/1000
hm = m/100
dam = m/10
dcm = m*10
cm = m*100
mm = m *1000
print('Essas são as variações de medida de {} metros: \n km = {} \n hm = {} \n dam = {} \n dcm = {:.0f} \n cm = {:.0f} \n mm = {:.0f}'.format(m,km,hm,dam,dcm,cm,mm))
