from flask import Flask, render_template, request, redirect, url_for

from flask import flash

from models.cliente import cadastrar_cliente, buscar_cliente, editar_cliente, listar_clientes, excluir_cliente

from models.produto import cadastrar_produto, buscar_produto, editar_produto, listar_produtos, excluir_produto

from models.pedido import cadastrar_pedido, listar_pedidos, buscar_pedido,buscar_itens_pedido, adicionar_produto, remover_produto_pedido, alterar_status_pedido, calcular_total_pedido, verificar_status_pedido, verificar_estoque_produto


app = Flask(__name__)

app.secret_key = "sistema_pedidos_123"


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/clientes')
def clientes():
    return render_template('clientes.html')


@app.route('/clientes/listar', methods=['GET'])
def listar_clientes_rota():
    clientes = listar_clientes()
    return render_template('clientes.html', pagina='listar', clientes=clientes)


@app.route('/clientes/cadastrar', methods=['GET', 'POST'])
def cadastrar_cliente_rota():

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cadastrar_cliente(nome, email)
        return redirect(url_for('listar_clientes_rota'))

    return render_template('clientes.html', pagina='cadastrar')



@app.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente_rota(id):


    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        editar_cliente(id, nome, email)
        return redirect(url_for('listar_clientes_rota'))


    cliente = buscar_cliente(id)

    return render_template('clientes.html', pagina='editar', cliente=cliente)


@app.route('/clientes/excluir/<int:id>', methods=['GET'])
def excluir_cliente_rota(id):

    excluir_cliente(id)
    
    return redirect(url_for('listar_clientes_rota'))


@app.route('/produtos')
def produtos_rota():
    return render_template('produtos.html')




@app.route('/produtos/listar', methods=['GET'])
def listar_produtos_rota():
    produtos = listar_produtos()
    
    return render_template('produtos.html', pagina='listar', produtos=produtos)



@app.route('/produtos/cadastrar', methods=['GET', 'POST'])
def cadastrar_produto_rota():

    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        estoque = int(request.form['estoque'])
        cadastrar_produto(nome, preco, estoque)
        return redirect(url_for('listar_produtos_rota'))

    return render_template('produtos.html', pagina='cadastrar')


@app.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto_rota(id):
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        editar_produto(id, nome, preco,)
        return redirect(url_for('listar_produtos_rota'))


    produto = buscar_produto(id)

    return render_template('produtos.html', pagina='editar', produto=produto)


@app.route('/produtos/excluir/<int:id>', methods=['GET'])
def excluir_produto_rota(id):

    excluir_produto(id)
    
    return redirect(url_for('listar_produtos_rota'))


@app.route('/pedidos')
def pedidos_rota():

    return render_template('pedidos.html')


@app.route('/pedidos/cadastrar', methods=['GET', 'POST'])
def cadastrar_pedido_rota():

    if request.method == 'POST':
        cliente_id = int(request.form['cliente_id'])
        cadastrar_pedido(cliente_id)
        return redirect(url_for('pedidos_rota'))

    clientes = listar_clientes()

    return render_template('pedidos.html', pagina='cadastrar', clientes=clientes)




@app.route('/pedidos/listar', methods=['GET'])
def listar_pedidos_rota():
    pedidos = listar_pedidos()

    for pedido in pedidos:
        total = calcular_total_pedido(pedido['id'])
        pedido['total'] = total

    return render_template('pedidos.html', pagina='listar', pedidos=pedidos)


@app.route('/pedidos/abrir/<int:id>', methods=['GET'])
def abrir_pedido_rota(id):
    pedido = buscar_pedido(id)
    produtos = listar_produtos()
    itens = buscar_itens_pedido(id)
    return render_template('pedidos.html', pagina='abrir', pedido=pedido, produtos=produtos, itens=itens)



@app.route('/pedidos/<int:pedido_id>/adicionar_produto', methods=['POST'])
def adicionar_produto_rota(pedido_id):

    status = verificar_status_pedido(pedido_id)

    if status == "Cancelado" or status == "Finalizado":

        flash("Não é possível adicionar produtos a um pedido cancelado ou finalizado.", "error")

        return redirect(url_for('abrir_pedido_rota', id=pedido_id))

    produto_id = int(request.form['produto_id'])

    quantidade = int(request.form['quantidade'])

    estoque_disponivel = verificar_estoque_produto(produto_id)

    if quantidade > estoque_disponivel:
        flash("Quantidade solicitada excede o estoque disponível.", "error")
        return redirect(url_for('abrir_pedido_rota', id=pedido_id))

    adicionar_produto(pedido_id, produto_id, quantidade)

    return redirect(url_for('abrir_pedido_rota', id=pedido_id))


@app.route('/pedidos/<int:pedido_id>/remover_item/<int:item_id>', methods=['GET'])
def remover_item_pedido_rota(pedido_id, item_id):
    remover_produto_pedido(pedido_id, item_id)

    return redirect(url_for('abrir_pedido_rota', id=pedido_id))

@app.route('/pedidos/<int:id>/alterar_status', methods=['GET', 'POST'])
def alterar_status_pedido_rota(id):

    if request.method == 'POST':
        status = request.form['status']

        alterar_status_pedido(id, status)

        return redirect(url_for('abrir_pedido_rota', id=id))

    return render_template('pedidos.html', pagina='alterar_status', pedido_id=id)
    

























if __name__ == '__main__':
    app.run(debug=True)