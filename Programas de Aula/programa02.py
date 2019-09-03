# Combinations, Permutations e Product - Intertools
# Combinação - Ordem não importa
# Permutação - Ordem importa
# >> Ambos não repetem valor
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabricio', 'Rose']

for gp in combinations(pessoas, 2):
    print(gp)
