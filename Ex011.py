print('Programa para cálculo de uma área de tinta para pintar uma parede')
l=float(input('Digite a largura da parede: '))
h=float(input('Digite a altura da parede: '))
a=l*h
l=(a/2)
la=int(l/3.6)
print('A área da parede é de {} m2 e sera necessário {} litros de tinta para pintá-la ou {} latas de tinta'.format(a,l,la))
