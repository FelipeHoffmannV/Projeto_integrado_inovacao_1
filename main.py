# Importando banco de dados Sqlite3
import sqlite3

# Classe que cria o objeto produto
class ItemEstoque:
    def __init__(self, nome, categoria, quantidade, preco, posicao):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.posicao = posicao


# Classe para gerenciamento do estoque

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
            posicao TEXT NOT NULL
        )
        ''')
        self.conn.commit()


# funcão para adicionar produtos ao banco de dados
    def adicionar_produto(self, produtos):
        self.cursor.execute('''
        INSERT INTO produtos (nome, categoria, quantidade, preco, posicao)
        VALUES (?, ?, ?, ?, ?)
        ''', (produtos.nome, produtos.categoria, produtos.quantidade, produtos.preco, produtos.posicao))
        self.conn.commit()

    # função para remover produtos da tabela do banco de dados
    def remover_produto(self, produto_id):
        self.cursor.execute('''DELETE FROM produtos WHERE id = ?''', (produto_id,))
        self.conn.commit()

    # funçãopara alterar quantidade de produtos
    def alterar_quantidade(self,produto_id, nova_quantidade):
            self.cursor.execute(f''' UPDATE produtos SET quantidade = {nova_quantidade} WHERE id = {produto_id} ''')
    
    # função para alterar preço dos produtos
    def alterar_preco(self, produto_id, novo_preco):
        self.cursor.execute(f''' UPDATE produtos SET preco = {novo_preco} WHERE id = {produto_id} ''')

# funcão para consultar produtos no banco de dados
    def consultar_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

# Fechanco conexão com o banco de dados.
    def Fechar_conexao(self):
        self.conn.close()


# Inicio da lógica para selecionar o que fazer no sistema.

# Variável que recebe a chave para interagir com o estoque
controle = GerenciamentoEstoque()

while True:
    print('Sistema de gerenciamento de estoque')
    print('---------------------------------------------------')
    print('Para cadastrar um novo produto digite o número 1')
    print('---------------------------------------------------')
    print('Para remover um produto digite o número 2')
    print('---------------------------------------------------')
    print('Para alterar a quantidade de um produto digite o número 3')
    print('---------------------------------------------------')
    print('Para alterar o preço de um produto digite o número 4')
    print('---------------------------------------------------')
    print('Para vizualizar seu estoque digite o número 5')
    print('---------------------------------------------------')
    print('Ao terminar as atividades no sistema digite 6 para encerrar')
    print('---------------------------------------------------')

    atividade = int(input('Digite o número correspondente ao que deseja fazer: '))

    if atividade == 6:
        print('Encerrando....')
        break
    elif atividade == 1:
        produto = ItemEstoque(input('Digite o nome do produto: '), input('Digite a categoria do produto (exemplo: Celular, Computador, Carregador, etc): '), int(input('Digite a quantidade que será adicionado ao estoque (POR FAVOR UTILIZE APENAS NÚMEROS INTEIROS.): ')), float(input('Digite o valor do produto: ')), input('Digite a posição aonde este produto será alocado no estoque (exemplo: Setor A, Fila C, Posição C): '))
        controle.adicionar_produto(produto)
        print('Produto adicionado ao seu estoque com sucesso!!!')
        continue

    elif atividade == 2:
        controle.remover_produto(int(input('Digite o identificador único do produto a ser removido: ')))
        print('Produto removido do seu estoque com sucesso!!')
        continue

    elif atividade == 3:
        controle.alterar_quantidade(int(input('Digite o identificador único do produto que deseja alterar a quantidade em estoque: ')), int(input('Digite o valor da nova quantidade: ')))
        print('Qantidade alterada com sucesso!!')
        continue
    
    elif atividade == 4:
        controle.alterar_preco(int(input('Digite o identificador único do produto que deseja alterar o preço: ')), float(input('Digite o novo preço do produto: ')))
        print('Preço do produto alterado com sucesso!!')

    elif atividade == 5:
        produtos = controle.consultar_produtos()
        for produto in produtos:
            print(f'ID: {produto[0]}, nome: {produto[1]}, categoria: {produto[2]}, quantidade:{produto[3]}, preço: {produto[4]}, Localização: {produto[5]}')

    else:
        print('Número digitado não corresponde a uma ação no sistema. Por favor tente um dos números listados abaixo!')
        print('______________________________________________________________________________________________________________________')

