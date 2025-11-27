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
CREATE TABLE IF NOT EXISTS alunos(
id INTEGER NOT NULL PRIMARY KEY,
nome TEXT NOT NULL,
idade INTEGER,
email TEXT);   

""")

conexao.execute("""
INSERT INTO alunos (nome,idade,email) VALUES 
                ("eduarda",16, "eduarda@gmail.com" ),
                ("victor", 16, "victorhugo@gmail.com"),
                ("gabriel", 18, "gabrielopes@gmail.com"),
                ("sarita" , 17, "sarita@gmail.com")
""")
lista_alunos = conexao.execute ("SELECT * FROM alunos").fetchall()
print ("alunos:", lista_alunos)

aluno = conexao.execute("SELECT * FROM alunos WHERE id = 3").fetchone()
print("Aluno:", aluno)

conexao.execute ("UPDATE alunos SET nome = 'victor' WHERE nome = 'gabriel' ")

listar_alunos = conexao.execute ("SELECT * FROM alunos "). fetchall ()
print ("alunos:" , lista_alunos)

conexao.execute("DELETE FROM alunos WHERE id=3")