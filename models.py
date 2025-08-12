from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType # Biblioteca que permite a definição de strings especiais para serem utilizadas dentro da entrada de infomação do usuário

# Cria a conexão do seu banco de dados/engine
db = create_engine("sqlite:///banco.db")

# Cria a base do banco de dados
Base = declarative_base()

# Cria as classes/tabelas do banco de dados

# Tabela de Usuário
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False) # "nullable funciona como um required, impedindo que dados sejam adicionados sem a presença de do dados específico
    nome = Column("nome", String)
    email = Column("e-mail", String)
    senha =  Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False) 

    def __init__(self, nome, email, senha, admin, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# Tabela de Pedido
class Pedido(Base):
    __tablename__  = "pedidos"

    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
    # itens = 

# Tabela de ItensPedido
class ItemPedido(Base):
    __tablename__ = "itens_pedidos"

    # BORDA_PEDIDO = (
    #     ("SEM BORDA", "SEM BORDA"),
    #     ("COM BORDA", "COM BORDA")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("qtd", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    tem_borda = Column("tem_borda", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, tem_borda, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.tem_borda = tem_borda
        self.preco_unitario = preco_unitario
        self.pedido = pedido

# Executa a criação dos metadados do banco 
