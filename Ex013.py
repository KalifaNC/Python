print('Programa para cálculo novo salário com aumento de 15%')
s=float(input('Digite o valor do salário: R$ '))
a=(s*15)/100
ns=s+a
print('O salário de R${:.2f} com aumento de 15 porcento é de R${:.2f}'.format(s,ns))

