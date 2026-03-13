from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Aluno(Base):

    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    idade = Column(Integer)
    curso = Column(String(100))

    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def __repr__(self):
        return f"Nome={self.nome} - Idade={self.idade} - Curso={self.curso}"
    
engine = create_engine("sqlite:///escola.db", echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


aluno1 = Aluno("Lucas Silva", 22, "Engenharia de Software")
session.add(aluno1)

aluno2 = Aluno("Mariana Costa", 19, "Ciência da Computação" )
session.add(aluno2)

aluno3 = Aluno("Caio Santos", 18, "Segurança da Informação")
session.add(aluno3)

aluno4 = Aluno("Roberta Silva", 25, "Análise e Desenvolvimento de Sistemas")
session.add(aluno4)

aluno5 = Aluno("Vinicius Lira", 30, "Redes de Computadores")
session.add(aluno5)

aluno6 = Aluno("Zé Rafael", 43, "Engenharia da Computação")
session.add(aluno6)

session.commit()

alunos_cadastrados = session.query(Aluno).all()
for a in alunos_cadastrados:
    print(a)

busca_aluno = session.query(Aluno).filter(Aluno.id == 1).first()
for b in busca_aluno:
    print(b)


update = session.query(Aluno).filter(Aluno.id == 1).first()
update.curso = "Back-end com o Gabriel"
session.commit()


romover_aluno1 = session.query(Aluno).filter(Aluno.id == 2).first()
session.delete()
session.commit()