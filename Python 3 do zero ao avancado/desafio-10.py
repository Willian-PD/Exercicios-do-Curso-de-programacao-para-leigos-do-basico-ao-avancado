def fizzBuzz(value):
    if(value % 3 == 0 and value % 5 == 0):
        return 'Fizz Buzz'
    if(value % 3 == 0):
        return 'Fizz'
    if(value % 5 == 0):
        return 'Buzz'
    return 'Valor não divisivél por 3 e nem por 5'
    

valor = float(input('Digite o valor a ser calculado: '))

print(fizzBuzz(valor))
