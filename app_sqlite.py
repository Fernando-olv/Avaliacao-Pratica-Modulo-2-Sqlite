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
CREATE TABLE  IF NOT EXISTS alunos (
 id INTEGER NOT NULL PRIMARY KEY,
 nome TEXT NOT NULL,
 idade INTEGER ,
 email TEXT);
""")
conexao.execute("""
INSERT INTO alunos (nome, idade,email) VALUES
                ("Hannah", 19, "hannah.game_play@gmail.com"),
                ("Diego", 20, "apenas_uma_camponesa@gmail.com"),
                ("Samuel", 1000000, "coitadinho_games@gmail.com"),
                ("Thiago", 16, "vai_menino@gmail.com"),
                ("Enzo", 19, "en70_play@gmail.com"),
                ("Ketelin",15, "ketelin_games@gmail.com");
""")

lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:", lista_alunos)


aluno = conexao.execute("SELECT * FROM alunos WHERE id = 3").fetchall()
print("Aluno 3", aluno)


conexao.execute("UPDATE alunos SET nome = 'Samuca' WHERE nome = 'Samuel' ")

lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:", lista_alunos)

conexao.execute("DELETE FROM alunos WHERE nome = 'Ketelin' ").fetchall()
lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:", lista_alunos)




