from math import pow
nome = str(input('Digite o seu nome: '))
idade = int(input('Digite o ano do seu nascimento: '))
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
ano = int(input('Digite o ano atual: '))

print(f'Nome: {nome}\n',
    f'Idade: {ano - idade}\n',
    f'Altura: {idade}\n',
    f'Peso: {peso:.2f}\n',
    f'IMC: {peso / pow(altura, 2):.2f}'
    )
