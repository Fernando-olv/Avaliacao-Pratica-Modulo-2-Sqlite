## 🔹 Parte 2 – CRUD com Python e SQLite

### 🎯 Critérios de Correção
O script deve implementar as operações **CRUD** na tabela `alunos`.

---

### 📌 Checklist

#### 1) Criar banco de dados  
- [ ] Criou o banco `escola.db` usando `sqlite3.connect()`.  
- [ ] Conexão e cursor foram criados corretamente.  

#### 2) Criar tabela `alunos`  
- [ ] Usou `CREATE TABLE`
- [ ] Seguiu o diagrama especificado (`id`, `nome`, `idade`, `email`).  
- [ ] Definiu `id` como **PRIMARY KEY**.  
- [ ] Respeitou os tipos corretos (TEXT, INTEGER, etc.).  

#### 3) Inserir registros  
- [ ] Usou `INSERT INTO alunos (...) VALUES (?, ?, ?)` com parâmetros.  
- [ ] Inseriu pelo menos 2 ou 3 registros de exemplo.   

#### 4) Listar todos  
- [ ] Usou `SELECT * FROM alunos`.  
- [ ] Exibiu os registros no console.  

#### 5) Buscar por ID  
- [ ] Criou consulta `SELECT * FROM alunos WHERE id = ?`.  
- [ ] Exibiu corretamente o resultado da busca.  

#### 6) Atualizar registros  
- [ ] Usou `UPDATE alunos SET ... WHERE id = ?`.  
- [ ] Fez `conn.commit()` após atualização.  
- [ ] Mostrou o registro atualizado no console.  

#### 7) Deletar registros  
- [ ] Usou `DELETE FROM alunos WHERE id = ?`.  
- [ ] Fez `conn.commit()` após exclusão.  
- [ ] Confirmou a exclusão listando os registros restantes.  

---
