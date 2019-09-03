def func(funcao, *args, **kwargs):
    print(funcao(*args, **kwargs))


def func2(arg):
    return f'Oi {arg}!'


def func3(arg, arg2):
    return f'{arg} {arg2}!'


func(func2, 'Willian')
func(func3, 'Olá', 'Willian')
