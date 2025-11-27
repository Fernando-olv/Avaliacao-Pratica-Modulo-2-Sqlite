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
email TEXT);
""")
conexao.execute(""" INSERT INTO Alunos (nome, idade,email) VALUES
                ("Samuel",12,"samuelvictor@gmail"),
                ("Pablo maia", 289,"PAblo777@gmail.com"),
                ("Paolo guerra", 11289,"luizkjkkkkk@gmail.com") 


""")
#listar todos 

lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("alunos", lista_alunos)

#buscar

aluno = conexao.execute("SELECT * FROM alunos WHERE id = 3").fetchone()
print("alunos 3", aluno)

#atualizar

conexao.execute("UPDATE alunos SET nome = 'matteo' WHERE nome = 'Lana'")
lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:",lista_alunos)

#deletar
conexao.execute("DELETE FROM Alunos WHERE nome = 'Samuel' ")
lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("alunos:", lista_alunos)
















