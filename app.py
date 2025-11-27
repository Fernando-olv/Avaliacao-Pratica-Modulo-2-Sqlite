
import sqlite3

conexao = sqlite3.connect("escola.db")

conexao.execute("""
CREATE TABLE IF NOT EXISTS alunos VALUES (
id INTEGER NOT NULL PRIMARY KEY,
nome TEXT NOT NULL, 
idade INTEGER,
email TEXT UNIQUE NOT NULL); 
""")

conexao.execute("""
INSERT OR IGNORE INTO alunos (nome, idade, email) VALUES
("Ana Luisa", 17, "analuisa@gmail.com"),
("Clara Nunes", 19, "unesclara@gmail.com"),
("Paolo Gustavo", 16, "gustavopaolo@gmail.com");
""")

# Exibe todos os alunos 

lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:", lista_alunos)

#Exibe o nome do aluno com ID

aluno = conexao.execute("SELECT nome, idade, email FROM alunos where id = 1;")
print("Aluno 1:", aluno)

