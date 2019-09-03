from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'},
]
alunos.sort(key = lambda item: item['nota'])
alunos_agrupados = groupby(alunos, lambda item: item['nota'])

for item, itens in alunos_agrupados:
    va1, va2 = tee(itens)

    print(f'group: {item}')
    
    for aluno in va1:
        print(f'\t{aluno}')
    
    quantidade = len(list(va2))
    print(f'{quantidade} alunos tiraram nota {item}')
    print()