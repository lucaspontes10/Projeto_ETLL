import numpy as np
import mysql.connector
import pandas as pd

#Criando conexão entre Python e MySQL
conexao = mysql.connector.connect(
    host='localhost',
    database='Dataset',
    user='root',
    password='123456789'
)

##Verifique o tipo de objeto retornado pela conexão
print(type(conexao))  # Deve ser <class 'mysql.connector.connection_cext.CMySQLConnection'>

#LENDO O CSV
df = pd.read_csv('euro_lineups.csv')
df = df.replace({np.nan: None})
df = df.fillna(0)


#Criando um cursor para executar comandos SQL
cursor = conexao.cursor()


tablename = 'euro_lineups'
cols = ",".join([str(i) for i in df.columns.tolist()])

# Iterar pelas linhas do DataFrame e inserir os dados
for i, row in df.iterrows():
    sql = f"INSERT INTO {tablename} ({cols}) VALUES ({','.join(['%s' for _ in row])})"
    cursor.execute(sql,tuple(row))

   # print(tuple(row))
                   
# Confirmar as inserções
conexao.commit()

# Fechar a conexão
cursor.close()
conexao.close()

print("Dados inseridos com sucesso!")