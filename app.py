
# Importação das tecnologias utilizadas
from flask import Flask, render_template, request, redirect, url_for
# Importação do gerenciador de banco de dados SQLITE 3
import sqlite3

# Inicialização do app flask
app = Flask(__name__)

# Classe para gerenciamto de estoque
class GerenciamentoEstoque:
    def __init__(self, db_name='estoque.db',):
        self.conn = sqlite3.connect(db_name,  check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.criar_tabela()
    # Função para criar tabela no banco de dados
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL,
                posicao TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    # Função para adicionar produto a tabela 
    def adicionar_produto(self, nome, categoria, quantidade, preco, posicao):
        self.cursor.execute('''
            INSERT INTO produtos (nome, categoria, quantidade, preco, posicao)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, categoria, quantidade, preco, posicao))
        self.conn.commit()
    # Função para remover produto do banco de dados
    def remover_produto(self, produto_id):
        self.cursor.execute('''DELETE FROM produtos WHERE id = ?''', (produto_id,))
        self.conn.commit()
    # Função para alterar quantidade dos produtos no banco de dados
    def alterar_quantidade(self, produto_id, nova_quantidade):
        self.cursor.execute('''UPDATE produtos SET quantidade = ? WHERE id = ?''', (nova_quantidade, produto_id))
        self.conn.commit()
    # Função para alterar oreço dos produtos
    def alterar_preco(self, produto_id, novo_preco):
        self.cursor.execute('''UPDATE produtos SET preco = ? WHERE id = ?''', (novo_preco, produto_id))
        self.conn.commit()
    # Função para consultar os produtos presentes em estoque
    def consultar_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()
    # Fechando conexão com banco de dados
    def fechar_conexao(self):
        self.conn.close()

# Variável inicia a instancia de gerenciamento
estoque = GerenciamentoEstoque()

# Rota principal 
@app.route('/')
def index():
    return render_template('index.html')

# Rota para adicionar produtos
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        quantidade = request.form['quantidade']
        preco = request.form['preco']
        posicao = request.form['posicao']
        estoque.adicionar_produto(nome, categoria, quantidade, preco, posicao)
        return redirect(url_for('index'))
    return render_template('adicionar.html')

# Rota para remover produtos
@app.route('/remover', methods=['GET', 'POST'])
def remover():
    if request.method == 'POST':
        produto_id = request.form['produto_id']
        estoque.remover_produto(produto_id)
        return redirect(url_for('index'))
    return render_template('remover.html')

# Rota para alterar características doo produto 
@app.route('/alterar', methods=['GET', 'POST'])
def alterar():
    if request.method == 'POST':
        produto_id = request.form['produto_id']
        nova_quantidade = request.form['nova_quantidade']
        novo_preco = request.form['novo_preco']
        estoque.alterar_quantidade(produto_id, nova_quantidade)
        estoque.alterar_preco(produto_id, novo_preco)
        return redirect(url_for('index'))
    return render_template('alterar.html')


# Rota para consultar produtos
@app.route('/consultar')
def consultar():
    produtos = estoque.consultar_produtos()
    return render_template('consultar.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
