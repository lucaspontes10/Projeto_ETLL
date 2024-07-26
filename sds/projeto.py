import mysql.connector
import pandas as pd

#criando conexão entre python e mysql. 
conexao =mysql.connector.connect(host='localhost',
                                database='Dataset',
                                user='root',
                                password='123456789'),  

print(conexao)




