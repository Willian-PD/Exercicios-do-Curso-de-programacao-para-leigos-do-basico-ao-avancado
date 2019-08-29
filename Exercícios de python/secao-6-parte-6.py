e = 0.0
c = input('Digite o código do operário: ')
n = float(input('Digite a quantidade de horas trabalhadas do operário: '))

if (n > 50.0):
    e = n - 50.0
    n += e

print(f'Salário do operário: R${n * 10.0:.2f}')
print(f'Bônus este mês: R${e * 20.0:.2f}')
