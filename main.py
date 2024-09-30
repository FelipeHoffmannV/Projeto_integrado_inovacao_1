# Biblioteca sqlite3
import sqlite3

# Estrutura de dados com conexão ao banco de dados.

class ItemEstoque:
    def __init__(self, nome, categoria, quantidade, preco, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

# Conexão ao banco de dados
class GerenciamentoEstoque:
    def __init__(self, db_name = 'estoque.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

# Criação de uma tabela no bando de dados
    def criar_tabela(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL,
            localizacao TEXT NOT NULL
        )
        ''')
        self.conn.commit()


# funcão para adicionar produtos ao banco de dados
    def adicionar_produto(self, produtos):
        self.cursor.execute('''
        INSERT INTO produtos (nome, categoria, quantidade, preco, localizacao)
        VALUES (?, ?, ?, ?, ?)
        ''', (produtos.nome, produtos.categoria, produtos.quantidade, produtos.preco, produtos.localizacao))
        self.conn.commit()

# função para remover produtos da tabela do banco de dados
    # função para remover produtos da tabela do banco de dados
    def remover_produto(self, produto_id):
        self.cursor.execute('''DELETE FROM produtos WHERE id = ?''', (produto_id,))
        self.conn.commit()

# funcão para consultar produtos no banco de dados
    def consultar_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

# Fechanco conexão com o banco de dados.
    def Fechar_conexao(self):
        self.conn.close()





# testes

controle = GerenciamentoEstoque()

Produto1 = ItemEstoque('Motorola Moto G-10' , 'Celulares', 50 , 250.25 , 'setor C, fila M, posicao 15')
Produto2 = ItemEstoque('Notebook Asus Zenbook' , 'Computadores', 73 , 1500 , 'setor N, fila Z, posicao 26')

controle.adicionar_produto(Produto1)
controle.adicionar_produto(Produto2)

# Teste para remover produto
controle.remover_produto(1)


produtos = controle.consultar_produtos()
for produto in produtos:
    print(f'ID: {produto[0]}, nome: {produto[1]}, categoria: {produto[2]}, quantidade:{produto[3]}, preço: {produto[4]}, Localização: {produto[5]}')
