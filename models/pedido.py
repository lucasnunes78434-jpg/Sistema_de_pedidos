from db import get_db

from models.produto import diminuir_estoque_produto, devolver_estoque_produto

def cadastrar_pedido( cliente_id):

    conexao = get_db()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO pedidos ( cliente_id,  status) VALUES (%s, %s)", ( cliente_id,"Aberto"))

    conexao.commit()
    cursor.close()  
    conexao.close()


def listar_pedidos():

    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT pedidos.id, clientes.nome AS cliente_nome, pedidos.status, pedidos.data
        FROM pedidos
        JOIN clientes ON pedidos.cliente_id = clientes.id
    """)

    pedidos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return pedidos


def buscar_pedido(id):

    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT pedidos.id, clientes.nome AS cliente_nome, pedidos.status, pedidos.data
        FROM pedidos
        JOIN clientes ON pedidos.cliente_id = clientes.id
        WHERE pedidos.id = %s
    """, (id,))

    pedido = cursor.fetchone()

    cursor.close()
    conexao.close()

    return pedido

def adicionar_produto(pedido_id, produto_id, quantidade):
    conexao = get_db()
    cursor = conexao.cursor()



    # Buscar preço do produto
    cursor.execute("""
        SELECT preco 
        FROM produtos 
        WHERE id = %s
    """, (produto_id,))
    
    resultado = cursor.fetchone()
    preco = resultado[0]

    # Inserir item com preço
    cursor.execute("""
        INSERT INTO itens_pedidos (pedido_id, produto_id, quantidade, preco)
        VALUES (%s, %s, %s, %s)
    """, (pedido_id, produto_id, quantidade, preco))

    diminuir_estoque_produto(cursor, quantidade, produto_id)

    conexao.commit()
    cursor.close()
    conexao.close()


def buscar_itens_pedido(pedido_id):

    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT itens_pedidos.id, produtos.nome AS produto_nome, itens_pedidos.quantidade, itens_pedidos.preco
        FROM itens_pedidos
        JOIN produtos ON itens_pedidos.produto_id = produtos.id
        WHERE itens_pedidos.pedido_id = %s
    """, (pedido_id,))

    itens = cursor.fetchall()

    cursor.close()
    conexao.close()

    return itens


def remover_produto_pedido(pedido_id, item_id):

    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT produto_id, quantidade
        FROM itens_pedidos
        WHERE id = %s AND pedido_id = %s
    """, (item_id, pedido_id))

    item = cursor.fetchone()
    produto_id = item['produto_id']
    quantidade = item['quantidade']

    devolver_estoque_produto(cursor, produto_id, quantidade)

    cursor.execute("""
        DELETE FROM itens_pedidos
        WHERE pedido_id = %s AND id = %s
    """, (pedido_id, item_id))

    conexao.commit()
    cursor.close()
    conexao.close()

def alterar_status_pedido(id, status):
    conexao = get_db()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE pedidos
        SET status = %s
        WHERE id = %s
    """, (status, id))

    conexao.commit()
    cursor.close()
    conexao.close()

def calcular_total_pedido(pedido_id):
    conexao = get_db()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT preco, quantidade
        FROM itens_pedidos
        WHERE pedido_id = %s
    """, (pedido_id,))

    itens = cursor.fetchall()

    total = 0

    for item in itens:
        preco = item[0]
        quantidade = item[1]

        total = total + (preco * quantidade)

    cursor.close()
    conexao.close()

    return total

def verificar_status_pedido(pedido_id):
    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT status
        FROM pedidos
        WHERE id = %s
    """, (pedido_id,))

    resultado = cursor.fetchone()
    status = resultado['status']

    cursor.close()
    conexao.close()

    return status

def verificar_estoque_produto(produto_id):
    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT estoque
        FROM produtos
        where id = %s
    """, (produto_id,))

    resultado = cursor.fetchone()
    estoque = resultado['estoque']

    cursor.close()
    conexao.close()

    return estoque
