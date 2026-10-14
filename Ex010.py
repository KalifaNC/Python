print("Esse programa calcula quantos dolares você pode comprar com uma quantia em reais ")
r=float(input('Digite a quantia em reais na carteira: '))
d=(r/3.27)
print('Com R${:.2f} você pode comprar US${:.2f}'.format(r,d))

