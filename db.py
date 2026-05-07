import mysql.connector

def get_db():
    conexao = mysql.connector.connect(
        host="localhost",   
        user="root",
        password="",        
        database="sistema_pedidos"
    )
    return conexao

    

