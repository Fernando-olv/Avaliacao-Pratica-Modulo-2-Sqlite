"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""
import sqlite3

conexao = sqlite3.connect("escola.db")

conexao.execute("""
CREATE TABLE IF NOT EXISTS alunos (
id INTEGER NOT NULL PRIMARY KEY,
nome TEXT NOT NULL,
idade INTEGER,
email TEXT UNIQUE NOT NULL
);

""")

conexao.execute("""
INSERT INTO alunos (nome, idade, email) VALUES ("Joelma", 23, "joelma123@emailpontocom"),
                ("Bartolomeu", 87,"bartoeomeu@emailpontocom"),
                ("Catarina", 22, "racatinadarina@emailpontocom")
""")

lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:", lista_alunos)

lista_alunos = conexao.execute("SELECT * FROM alunos").fetchone()
print("Alunos:", lista_alunos)
# poderia ser também > aluno = conexao.execute("SELECT * FROM alunos WHERE nome = 'José' "). fetchall \/ (print("Alunos Joelma:",aluno)

aluno = conexao.execute("DELETE FROM alunos WHERE nome = 'Joelma' ")
print("Aluno José:",aluno)