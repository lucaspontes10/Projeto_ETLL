# Solicita ao usuário que digite dois valores entre 01 e 99
Primeiro = int(input("Digite o primeiro valor (entre 01 e 99): "))
Segundo = int(input("Digite o segundo valor (entre 01 e 99): "))

# Verifica se os valores estão dentro do intervalo válido (01 a 99)
if 1 <= Primeiro <= 99 and 1 <= Segundo <= 99:
    # Compara se o segundo valor é maior ou igual ao primeiro valor
    if Segundo >= Primeiro:
        print(f"O segundo valor ({Segundo}) é maior ou igual ao primeiro valor ({Primeiro}).")
    else:
        print(f"O segundo valor ({Segundo}) é menor que o primeiro valor ({Primeiro}).")
else:
    print("Os valores inseridos não estão no intervalo válido (01 a 99).")