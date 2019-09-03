from dados import produtos, pessoas, lista

# #nova_lista = map(lambda x: x * 2, lista)
# nova_lista = [x * 2 for x in lista]
# print(lista)
# print(list(nova_lista))

# for produto in produtos:
#     print(produto)

# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p


# preco = map(aumenta_preco, produtos)
# for i in preco:
#     print(i)

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)