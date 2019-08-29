numero = int(input('Digitr um valor negativo ou positivo: '))

if (numero % 2 == 0):
    print('Número par!')
    if(numero > 0):
        print('Número positivo!')
    else:
        print('Número negativo!')
else:
    print('Número ímpar!')
    if(numero < 0):
        print('Número negativo!')
    else:
        print('Número positivo!')
    