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
nome TEXT not NULL,
idade INTEGER,
email TEXT)

""")

conexao.execute("""
INSERT or IGNORE INTO alunos (nome, idade, email) VALUES
('gabriel', 22, "faverim@gmail"),
("nandinho", 40, "nandinho@gmail"),
("nega", 38, "nega@gmail");

 """)

#Exibir todos os alunos 
lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("alunos:", lista_alunos)

#Exibir o nome do aluno com 
aluno = conexao.execute("SELECT * FROM alunos WHERE nome = 'gabriel' ").fetchall()
print("aluno gabriel:", aluno)

#atualizar algum registro e mostrar ele atualizado
aluno = conexao.execute("UPDATE alunos SET nome = 'faverim' WHERE id = 1;").fetchall()
print("aluno",aluno)

conexao.execute("DELETE FROM alunos WHERE id = 2")





