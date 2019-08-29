from math import pow

n = []
q = []

for i in range(0, 4):
    n.append(float(input('Digite um valor: ')))

for i in range(0, 4):
    q.append(pow(n[i], 2))

if(q[2] >= 1000):
    print(f'{q[2]:.2f}')
else:
    i = 0
    while (i < 4):
        print(f'O quadrado de {n[i]:.2f} é {q[i]:.2f}')
        i += 1
