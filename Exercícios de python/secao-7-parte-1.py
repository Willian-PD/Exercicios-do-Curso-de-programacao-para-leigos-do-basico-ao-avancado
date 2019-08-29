maior = 0

valor = int(input('Digite um valor: '))
while (valor != 0):
    if (valor > maior):
        maior = valor
    valor = int(input('Digite um valor novamente: '))
print(f'O maior valor digitado foi {maior}')
