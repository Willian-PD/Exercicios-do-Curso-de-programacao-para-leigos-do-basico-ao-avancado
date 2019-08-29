from random import randrange
maior = -999
menor = 999
soma = 0

for i in range(1, 10 + 1):
    valor = randrange(0, 20)
    soma += valor
    if(valor > 0):
        if(valor > maior):
            maior = valor
        if(menor == -1 or valor < menor):
            menor = valor
    else:
        valor = randrange(0, 20)
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Média: {(soma / 10)}')
