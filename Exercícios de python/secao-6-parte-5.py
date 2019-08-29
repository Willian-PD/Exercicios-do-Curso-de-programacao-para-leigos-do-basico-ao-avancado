excesso = 0.0
multa = 0.0
peso = float(input('Digite quantos quilos de peixe você está carregando: '))

if (peso > 50):
    excesso = peso - 50
    multa = excesso * 4.00

print(f'Peso total da carga: {peso:.2f}kg')
print(f'Total excedido: {excesso:.2f}kg')
print(f'Total da multa: R${multa:.2f}')
