# 🏋️ Academia do Zé — API REST - Gestão de Academia

API REST desenvolvida em **Go (Golang)** utilizando o pacote nativo `net/http` e banco de dados **SQLite3**.  
*(ensina Node.js e Express pra nós, fessor!)*

---

##  Sobre o Projeto

Esta API gerencia o cadastro de uma academia. O sistema permite cadastrar planos de mensalidade e vincular alunos a esses planos. Cada aluno pertence a um plano específico (relação 1:N / Pai-Filho).

A API oferece um CRUD completo para o gerenciamento de alunos e planos, além de filtros avançados e buscas com `JOIN`.

---

##  Tabelas do Banco de Dados

### Tabela `planos` (Pai)

| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | `INTEGER` | Chave primária (Autoincrement) |
| `nome` | `TEXT` | Nome do plano (ex: Plano Mensal Standard) |
| `preco` | `REAL` | Preço da mensalidade |

### Tabela `alunos` (Filho)

| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | `INTEGER` | Chave primária (Autoincrement) |
| `nome` | `TEXT` | Nome completo do aluno |
| `email` | `TEXT` | E-mail de contato |
| `plano_id` | `INTEGER` | Chave estrangeira → Aponta para `planos(id)` (`ON DELETE CASCADE`) |

**Relação:** Cada **Aluno** (Filho) está associado a um **Plano** (Pai). Um plano pode ter múltiplos alunos vinculados.

---

##  Como Rodar o Projeto

### Pré-requisitos
* **Go** (versão 1.22 ou superior)
* **GCC / CGO** ativado (necessário para o driver do SQLite `go-sqlite3`)

### Passos:

1. **Baixar as dependências do módulo Go:**
   ```bash
   go mod tidy

## Executar a aplicação

    go run main.go
    A API estará disponível em: http://localhost:8080

### Como testar:
    ### 1. Listar todos os planos
GET http://localhost:8080/planos

### 2. Criar um novo plano
POST http://localhost:8080/planos
Content-Type: application/json

{
    "nome": "Plano Black Anual",
    "preco": 199.90
}

### 3. Listar todos os alunos
GET http://localhost:8080/alunos

### 4. Criar um novo aluno
POST http://localhost:8080/alunos
Content-Type: application/json

{
    "nome": "Monkey D. Luffy",
    "email": "luffy@pirates.com",
    "plano_id": 1
}

### 5. Buscar aluno por ID
GET http://localhost:8080/alunos/1

### 6. Atualizar aluno por ID
PUT http://localhost:8080/alunos/1
Content-Type: application/json

{
    "nome": "Mateus Silva Atualizado",
    "email": "mateus.novo@email.com",
    "plano_id": 2
}

### 7. Listar alunos com o nome do Plano (JOIN)
GET http://localhost:8080/alunos/detalhes

### 8. Filtrar alunos por nome (LIKE)
GET http://localhost:8080/alunos/busca?nome=Mateus

### 9. Filtrar alunos por ID do Plano
GET http://localhost:8080/plano/1/alunos

### 10. Deletar um aluno por ID
DELETE http://localhost:8080/alunos/4

---
##  Integrantes

- **Mateus** — Criação do código  
- **Golang** — Me deu forças mentais para aguentar a vida  
