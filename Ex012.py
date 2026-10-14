print('Programa de calculo de novo preço com desconto de 5%')
p=float(input('Digite o preço de um produto: '))
d=(p*5)/100
np=p-d
print('O preço do produto com 5% de desconto é de R${:.2f}'.format(np))
