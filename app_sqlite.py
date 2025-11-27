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

# Criação da tabela alunos
conexao.execute("""

CREATE TABLE IF NOT EXISTS alunos(
id INTEGER NOT NULL PRIMARY KEY,
nome TEXT NOT NULL,
idade INTEGER,
email TEXT);

   """)

# Inserção 3 alunos 
conexao.execute("""
INSERT INTO alunos (nome, idade, email) VALUES
                ("Meilin", 12, "meimei@gmail.com"),
                ("Matteo", 14, "Teo@gmail.com"),
                ("Lana", 13, "Lala@gmail.com");
""")

# Listar todos
lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:", lista_alunos)

# Buscar id
aluno = conexao.execute("SELECT * FROM alunos WHERE id = 3"). fetchone()
print("Alunos 3", aluno)

# Atualizar registros
conexao.execute("UPDATE alunos SET nome = 'Matteo' WHERE nome = 'Lana'")
lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:", lista_alunos)

# Deletar registros
conexao.execute("DELETE FROM alunos WHERE nome = 'Matteo'")
lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:", lista_alunos)
