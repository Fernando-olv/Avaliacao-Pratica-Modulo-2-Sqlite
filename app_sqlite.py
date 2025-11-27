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
CREATE TABLE IF NOT EXISTS Alunos ( 
id INTEGER NOT NULL PRIMARY KEY , 
Nome TEXT NOT NULL,	
Idade INTEGER ,
Email TEXT );
""")

conexao.execute("""
INSERT INTO Alunos (Nome,Idade,Email)VALUES 
                ("Diego", 15, "pequena_camponesa@gmail.com"), 
                ("Guilherme", 16, "pai_de_familia@gmail.com"),
                ("Samuel", 16, "nike@gmail.com");

""")

lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:",lista_alunos)

Aluno = conexao.execute("SELECT * FROM Alunos WHERE id =2").fetchone()
print("Aluno 3", Aluno)

#atualizar registros
conexao.execute("UPDATE Alunos SET nome = 'Camponesa' WHERE Nome ='Diego'")

lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:",lista_alunos)

#Deletar registros
conexao.execute("DELETE FROM Alunos WHERE nome = 'Samuel'")
lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print("Alunos:",lista_alunos)
