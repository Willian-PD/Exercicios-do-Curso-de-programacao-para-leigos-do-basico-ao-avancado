tipoDefeito = 0
tipoDefeito1 = 0
tipoDefeito2 = 0
tipoDefeito3 = 0
count = 0
idMouse = 1

while (idMouse != 0):
    idMouse = int(input('Digite o id do mouse: '))
    count += 1
    defeito = int(input('Qual é o tipo de defeito?\n1 - Necessita da esfera\n2 - Necessita de limpeza\n3 - Necessita da troca do cabo ou do conector\n4 - Quebrado ou inutilizado\nDigite o valor aqui: '))
    if (defeito == 1):
        tipoDefeito += 1
    elif (defeito == 2):
        tipoDefeito1 += 1
    elif (defeito == 3):
        tipoDefeito2 += 1
    elif (defeito == 4):
        tipoDefeito3 += 1
    else:
        print(f'Opção inválida!\nDigite um valor de 1 a 4 de acordo com o problema encontrado!')

print(f'Total de mouses analisados: {count}')
print(f'Situação!\n1 - Necessita da esfera {tipoDefeito} {tipoDefeito / 100}%\n2 - Necessita de limpeza {tipoDefeito1} {tipoDefeito1 / 100}%\n3 - Necessita da troca do cabo ou do conector {tipoDefeito2} {tipoDefeito2 / 100}%\n4 - Quebrado ou inutilizado {tipoDefeito3} {tipoDefeito3 / 100}%')
