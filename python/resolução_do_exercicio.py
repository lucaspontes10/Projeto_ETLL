nome = input('digite o seu nome: ')
idade = input('digite sua idade: ')

if nome and idade :
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print( 'seu nome contem espaços')

    else:
        ('seu nome não contem espaços')

print(f'a primeira letra do seu nome é {nome[0]}')
print(f'a ultima letra do seu nome é {nome[-1]}')


