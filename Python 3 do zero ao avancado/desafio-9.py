def somaPercentual(num, porcent):
    if(porcent > 0):
        porcent /= 100
    return num * (1 + porcent)
    

valor = float(input('Digite o valor a ser calculado: '))
porcentagem = float(input('Digite a porcentagem a ser adicionada: '))

print(somaPercentual(valor, porcentagem))
