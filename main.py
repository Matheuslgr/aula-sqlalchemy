# instalar o sqlalchemy
# importar a bliblioteca responsavel por criar a conexao com o banco
from sqlalchemy import create_engine


# Importa os tipos de dados das colunas do banco
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importar a classe base usada para criar os modelos orm
from sqlalchemy.orm import declarative_base

# Importar a ferramenta para criar ssesões no banco
from sqlalchemy.orm import sessionmaker

# Criar a classe base do orm

Base = declarative_base()

# Classe = tabela no banco
# Atributo = coluna
# Objeto = linha de tabela


# Classe Produto representando a tebela do banco
class Produto(Base):
    #nome da tabela
    __tablename__ = "produtos"

    #Criar a coluna de ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # coluna nome
    nome = Column(String(100))

    #coluna de preço
    preco = Column(Float)

    #coluna de estoque
    estoque = Column(Integer)

    #coluna de ativo
    ativo = Column(Boolean)

    #método contrustor
    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo

    def __repr__(self):
        return f"produto (id= {self.id} - nome={self.nome} - preço={self.preco} - estoque={self.estoque} - ativo={self.ativo})"

#Criar a conexão
# log do banco de dados pra ativar = 
engine = create_engine("sqlite:///estoque.db", echo=False)

#Crias as tabelas - se ainda não existirem
Base.metadata.create_all(engine)

#Criar uma fabrica de sessões
Session = sessionmaker(bind=engine)

#Criar um carrinho (sessão ativa no banco)
session = Session()

#Crud - Cadastrar
#como criar um objeto

produto1 = Produto("gpro superlight 2", 2000, 50, True)
session.add(produto1)

produto2 = Produto("teclado magnetico", 1000, 10, True)
session.add(produto2)

produto3 = Produto("iphone 17 pro max", 7000, 5, True)
session.add(produto3)

produto4 = Produto("macbook", 1000, 34, True)
session.add(produto4)

produto5 = Produto("tablet", 3100, 11, True)
session.add(produto5)

produto6 = Produto("gpro superlight x", 2340, 23, True)
session.add(produto6)

#Salvar no banco
session.commit()

# # Buscar todos os produtos - listar
# produtos = session.query(Produto).all()
# #mostrar as infomacoes formatadas
# for produto in produtos:
#     print(produto)

# Buscar produtos pelo filter - listar
# buscar_produto = session.query(Produto).filter(Produto.id == 3).all()
# print(buscar_produto)


# #Buscar os produtos do estoque abaixo de 10
# estoque = session.query(Produto).filter(Produto.estoque < 10).all()
# print(estoque)


#Busca parcial - considera letras maiúsculas e minúsculas
# busca_parcial = session.query(Produto).filter(Produto.nome.like("%superlight%")).all()
# print(busca_parcial)

#Buscar id ou nomes
# buscar_produto2 = session.query(Produto).filter_by(id=4).first()
# print(buscar_produto2)

# Top produtos com estoque baixo - organizando a busca
top_produtos = session.query(Produto).order_by(Produto.estoque).all() #ordem cresente = menor pro maior
top_produtos2 = session.query(Produto).order_by(Produto.estoque.desc()).all() #ordem descresente = maior pro menor
# for p in top_produtos2:
#     print(p)


#limitando a quantidade de registro
top_produtos3 = session.query(Produto).order_by(Produto.estoque).limit(3).all()
# for p in top_produtos3:
#     print(p)

# Contar registro - contar as linhas do db
qtd = session.query(Produto).count()
# print(qtd)


# UPDATE - Atualizar registro no db

update = session.query(Produto).filter(Produto.id == 4).first()

#Atulizar um registro
# update.nome = "macbook pro"
# session.commit()

# Deletar algo db

remover_produto = session.query(Produto).filter(Produto.id == 4).first()
session.delete(remover_produto)
session.commit()