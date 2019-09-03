carrinho = []
soma = 0
i = 's'
while i != 'n':
    carrinho.append((input('Digite o nome do produto: '),
        float(input('Digite o preço do produto: '))))
    print(carrinho)
    i = input('Deseja continuar? - s/n: ')

soma = sum([valor[1] for valor in carrinho])

print(f'Total a pagar: R${soma:.2f}')