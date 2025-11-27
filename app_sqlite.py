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

#CRIAR A TABELA 
conexao.execute("""
CREATE TABLE  IF NOT EXISTS alunos (
id INTEGER NOT NULL PRIMARY KEY, 
nome TEXT NOT NULL,
idade INTEGER,
email TEXT UNIQUE NOT NULL
);
                      
""")

#INSERIR 3 ALUNOS NA TABELA 
conexao.execute ("""
INSERT OR IGNORE INTO alunos (nome, idade, email) VALUES 
("Fernanda", "15", "fernanda@aluna" ),
("Matheus", "15", "mathues@aluno"),
("Jessica", "15", "jessica@aluna");
                 
""")


#EXIBIR TODOS OS ALUNOS 
lista_alunos = conexao.execute ("SELECT * FROM alunos").fetchall()
print("Alunos:", lista_alunos)


#LISTAR SÓ UM ALUNO COM O ID
lista_alunos = conexao.execute ("SELECT * FROM alunos WHERE id = 1").fetchall()
print ("id = 1", lista_alunos)


#ATUALIZAR REGISTRO 
conexao.execute ("UPDATE alunos SET nome = 'Pedro', email = 'pedro@aluno' WHERE id = 2 ")

#DELETAR 1 REGISTRO 
conexao.execute ("DELETE FROM alunos WHERE id = 3")