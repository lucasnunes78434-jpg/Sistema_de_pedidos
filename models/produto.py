from db import get_db


def cadastrar_produto(nome, preco, estoque):

    conexao = get_db()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)", (nome, preco, estoque))

    conexao.commit()
    cursor.close()  
    conexao.close()


def listar_produtos():
    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT id, nome, preco, estoque FROM produtos")

    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produtos

def buscar_produto(id):

    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT id, nome, preco FROM produtos WHERE id = %s", (id,))

    produto = cursor.fetchone()

    cursor.close()
    conexao.close()

    return produto

def editar_produto(id, nome, preco,):
    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("UPDATE produtos SET nome = %s, preco = %s WHERE id = %s", (nome, preco, id))

    conexao.commit()

    cursor.close()
    conexao.close()

def excluir_produto(id):
    conexao = get_db()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))

    conexao.commit()

    cursor.close()
    conexao.close()

def diminuir_estoque_produto( cursor, quantidade,produto_id):
    
    cursor.execute("UPDATE produtos SET estoque = estoque - %s WHERE id = %s", (quantidade, produto_id))

def devolver_estoque_produto(cursor, produto_id, quantidade):
    
    cursor.execute("UPDATE produtos SET estoque = estoque + %s WHERE id = %s", (quantidade, produto_id))

    