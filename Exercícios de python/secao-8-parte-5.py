vetor = []
maiores50 = False
for i in range(0, 20):
    vetor.append(int(input('Digite um valor: ')))
    if (vetor[i] > 50):
        print(f'Valor {vetor[i]} maior que 50 na posição {i}!')
        maiores50 = True

if(maiores50 == False):
    print('Não existe valores maiores que 50!')
