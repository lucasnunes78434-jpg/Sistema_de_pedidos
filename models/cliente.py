from db import get_db

def cadastrar_cliente(nome, email):

    
    conexao = get_db()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, email)  VALUES (%s, %s)", (nome, email))

    conexao.commit()

    cursor.close()
    conexao.close()


# funçoes para buscar e editar clientes

def buscar_cliente(id):

    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT id, nome, email FROM clientes WHERE id = %s", (id,))

    cliente = cursor.fetchone()

    cursor.close()
    conexao.close()

    return cliente

def editar_cliente(id, nome, email):

    conexao = get_db()
    cursor = conexao.cursor()

    cursor.execute("UPDATE clientes SET nome = %s, email = %s WHERE id = %s", (nome, email, id))

    conexao.commit()

    cursor.close()
    conexao.close()

# fim das funçoes para buscar e editar clientes

def listar_clientes():

    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT id, nome, email FROM clientes")

    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()

    return clientes


def excluir_cliente(id):

    conexao = get_db()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))

    conexao.commit()

    cursor.close()
    conexao.close()
