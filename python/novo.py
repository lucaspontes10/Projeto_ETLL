nome = input('digite seu nome: ')
encontrar =  input ('digite oque deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')