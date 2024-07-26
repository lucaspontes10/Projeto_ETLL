numero_str = input(
     'vou dobrar o numero que você digitar :'
)

try:
   numero_float = float (numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2 :.2f}').

except:
   print('isso não é um numero')




'''
if numero_str.isdigit():
    numero_float = float (numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2 :.2f}')
else:
    print('isso não é um numero')