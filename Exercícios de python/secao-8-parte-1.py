vetor = [0, 0, 0, 0, 0]
pares = []
for i in vetor:
    vetor[i] = int(input('Digite um valor: '))
    if ((vetor[i] > 0) and (vetor[i] % 2 == 0)):
        pares.append(vetor[i])

print(f'{pares}')