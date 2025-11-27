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
 Id  INTEGER NOT NULL PRIMARY KEY,
 nome TEXT NOT NULL,
 idade INTEGER,
 email TEXT)                                             
                  
 """)
 
conexao.execute(""" 


INSERT OR IGNORE INTO alunos (nome, idade, email) VALUES
("Romario"),46,("romario@gmail.com"),
("Ronaldo"),43, ("ronaldo@gmail.com"),
("Bebeto"),47, ("bebeto@gmail.com");

""")
# Exibi todos os Alunos
lista_alunos = conexao.execute("select * FROM alunos").fetchall()
print("Alunos:", lista_alunos)
 
# Exibe o nome do aluno com id = 1 
aluno= conexao.execute("SELECT * FROM alunos WHERE nome = 'Romario'").fetchall()
print("Aluno ROMÁRIO:",aluno)

# Atualizar algum registro e mostrar ele atualizado
conexao.execute("UPDATE alunos SET nome = 'Ronaldinho' WHERE id = 2")
# Deletar 1 registro 
conexao.execute("DELETE FROM alunos WHERE id = 3")