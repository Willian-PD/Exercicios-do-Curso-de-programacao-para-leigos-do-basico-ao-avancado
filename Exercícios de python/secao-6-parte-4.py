altura = float(input('Digite a sua altura: '))
sexo = input('Digite a seu sexo: ')
if(sexo == 'M' or sexo == 'm'): 
    print(f'Seu peso ideal é {(72.7 * altura) - 58:.2f}')
elif(sexo == 'F' or sexo == 'f'):
    print(f'Seu peso ideal é {(62.1 * altura) - 44.7:.2f}')
