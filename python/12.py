import pandas as pd

funcionarios = {
    'Nome': ['João Silva', 'Maria Souza', 'José Ramos', 'Pedro Ferreira'],
    'Idade': [35, 40, 54, 39],
    'Tempo de Empresa': [3, 10, 15, 7],
}

dataframe = pd.DataFrame(funcionarios)

print (dataframe.head())
