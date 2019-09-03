nome = input('Digite o seu nome: ')

if len(nome) <= 4:
    print(f'{nome}, seu nome é pequeno!')
elif len(nome) > 4 and len(nome) <= 6:
    print(f'{nome}, seu nome é normal!')
elif len(nome) > 6:
    print(f'{nome}, seu nome é gigante!')
