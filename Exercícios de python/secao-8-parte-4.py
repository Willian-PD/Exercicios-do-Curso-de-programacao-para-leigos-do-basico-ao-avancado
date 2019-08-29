vetor = []
soma = 0
for i in range(0, 20):
    vetor.append(int(input('Digite um valor: ')))
    soma += vetor[i]

print(f'Total: {soma}')