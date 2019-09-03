string = '012345678901234567890123456789012345678901234567890123456789'
lista = list(string)
newString = str()
newLista = []
i = 0
while i < len(lista):
    newString = newString + lista[i]
    if lista[i] == '9':
        newLista.append(newString)
        newString = ''
    i += 1

print('.'.join(newLista))
