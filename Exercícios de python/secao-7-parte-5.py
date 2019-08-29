nome = input('Informe seu nome: ')
senha = input('Informe sua senha: ')
while(senha == nome):
    print('A senha não pode ser igual ao nome!')
    nome = input('Informe seu nome: ')
    senha = input('Informe seu senha: ')
