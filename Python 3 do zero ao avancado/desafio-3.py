hora = int(input('Digite a hora atual: '))

if hora >= 0 and hora <= 11:
    print(f'São {hora} hrs, bom dia!')
elif hora >= 12 and hora <= 17:
    print(f'São {hora} hrs, boa tarde!')
elif hora >= 18 and hora <= 23:
    print(f'São {hora} hrs, boa noite!')
