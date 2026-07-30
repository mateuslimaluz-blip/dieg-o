# Academia do Zé

API REST desenvolvida em Python com Flask e banco de dados SQLite.

**Disciplina:** Programação no Desenvolvimento de Sistemas **Dupla:** Mateus Lima e Golang

---

## 📋 Sobre o projeto

*Esta API gerencia uma academia. É possível cadastrar clientes e planos, sendo que cada cliente possui um Plano. A API permite listar, criar, atualizar, apagar e buscar registros.*

---

## 🗂️ Tabelas do banco

Descreva suas duas tabelas e como elas se relacionam.

### Tabela `[Planos]`

| Campo | Tipo | Descrição |
| :---- | :---- | :---- |
| id | INTEGER | Chave primária (gerada automaticamente) |
| nome | VARCHAR(50) | Nome do plano |
| descrição | TEXT | Descrição do Planos |
| preco | REAL | Preço do plano |

### Tabela `[clientes]`

| Campo | Tipo | Descrição |
| :---- | :---- | :---- |
| id | INTEGER | Chave primária (gerada automaticamente) |
| idade | INTEGER | idade do cliente |
| nome | VARCHAR(40) | nome do cliente |
| \[planoi\]\_id | INTEGER | Chave estrangeira → aponta para \[tabela\_pai\] |

**Relação:** cada \[filho\] pertence a um(a) \[pai\]. *(explique a relação do seu tema)*

---

## 🚀 Como rodar o projeto

\# 1\. Instalar o Flask (caso não tenha)

pip install flask

\# 2\. Rodar a API

python main.py

\# 3\. A API estará disponível em:

\# http://127.0.0.1:5000

O banco de dados (`[nome].db`) é criado automaticamente na primeira execução.

---

## 🛣️ Rotas da API

Liste todas as rotas que você criou. Exemplo:

### Planos \[pai\]

| Método | Rota | O que faz |
| :---- | :---- | :---- |
| GET | `/Planos` | Lista todos os planos |
| GET | `/planos/<id>` | Busca um planos pelo id |
| POST | `/planos` | Cria um novo plano |
| PUT | `/Planos/<id>` | Atualiza um plano |
| DELETE | `/planos/<id>` | Apaga um autor |

### Clientes \[filho\]

| Método | Rota | O que faz |
| :---- | :---- | :---- |
| GET | `/clientes` | Lista todos os clientes |
| POST | `/clientes` | Adiciona um novo cliente |
| DELETE | `/clientes` | Deleta um cliente |

### Rotas especiais

| Método | Rota | O que faz |
| :---- | :---- | :---- |
| GET | `/Plano-descricao` | Mostra totalmente a descrição do plano |
| GET | `/clientes/planos/<id>` | Busca clientes com base no Id dos planos |

---

## 🧪 Como testar

Os testes estão no arquivo [`testes.http`](http://./testes.http) *(ou `testes.md` se usou curl)*.

Exemplo de requisição para criar um autor:

POST http://127.0.0.1:5000/autores

Content-Type: application/json

{

    "nome": "Machado de Assis"

}

---

## 👥 Integrantes

- \[Mateus\] — criação do código   
- \[Golang\] — Me deu forças mentais para aguentar a vida

