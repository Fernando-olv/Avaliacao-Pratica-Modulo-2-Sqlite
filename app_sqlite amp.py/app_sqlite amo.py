

import sqlite3

conexao = sqlite3.connect ("escola.db")

conexao.execute("""
CREATE TABLE IF NOT EXISTS Alunos (
id INTEGER NOT NULL PRIMARY KEY, 
nome TEXT NOT NULL, 
idade INTEGER, 
email TEXT);
""")

conexao.execute("""
INSERT INTO alunos (nome, idade, email) VALUES
               ("Bianca", 22, "bia@lindinha3.gmail.com"),
               ("Sarah", 19, "Sarete@saradona.gmail.com"),
               ("Duda", 23, "Maria@maravilha.gmail.com"), 
            ("Izabela", 20, "Izaboyceta@Lani.gmail.com");

""")
Lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print ("Alunos:", Lista_alunos)

aluno = conexao.execute("SELECT * FROM alunos WHERE id = 2").fetchone()
print("Aluno 3",aluno)

conexao.execute("UPDATE alunos SET nome = 'Bianca' WHERE nome = 'Sarah'")

Lista_alunos = conexao.execute("SELECT * FROM alunos").fetchall()
print ("Alunos:", Lista_alunos)

conexao.execut ("DELETE FROM alunos WHERE id=1")