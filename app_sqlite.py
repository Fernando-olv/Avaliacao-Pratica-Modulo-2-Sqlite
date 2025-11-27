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
conexao.execulte(""""
o alunos (nome,email,idade) VALUES ("jose",jose@gmail.com",50)        
                 ("carlos","carlos@gmail",25),
                 ("rubinho","rubinho@gmail",46);
""")
#exibe todos os alunos.
lista_alunos = conexao.execute("SELECT * FROM alunos"). fetvhall()
print("alunos:",lista_alunos)

#exibe o nome do aluno com ID =
aluno = conexao.execulte("SELECT * FROM alunos WHERE nome = 'jose' ").fetchall()
print("aluno jose:",aluno)

# atualizar algum registro e mostrar ele atualizado.


# deletar 1 registro.