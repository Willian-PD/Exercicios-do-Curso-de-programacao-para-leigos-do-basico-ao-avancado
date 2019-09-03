numero = input('Digite um valor inteiro: ')

if not numero.isdigit():
    print('Esse valor não é um inteiro!')
elif int(numero) % 2 == 0:
    print(f'{numero} é um inteiro par!')
else:
    print(f'{numero} é um inteiro impar!')
