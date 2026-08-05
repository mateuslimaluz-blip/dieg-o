package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"
	"strings"

	_ "github.com/mattn/go-sqlite3"
)

type Plano struct {
	ID    int     `json:"id"`
	Nome  string  `json:"nome"`
	Preco float64 `json:"preco"`
}

type Aluno struct {
	ID        int    `json:"id"`
	Nome      string `json:"nome"`
	Email     string `json:"email"`
	PlanoID   int    `json:"plano_id"`
	NomePlano string `json:"nome_plano"`
}

var db *sql.DB

func main() {
	var err error

	db, err = sql.Open("sqlite3", "./academia.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	criarTabelas()

	mux := http.NewServeMux()

	mux.HandleFunc("GET /planos", listarPlano) // Rotas Pais
	mux.HandleFunc("POST /planos", criarPlano)

	mux.HandleFunc("GET /alunos/busca", buscarAlunosPorNome) // Rotas Kids
	mux.HandleFunc("POST /alunos", criarAluno)
	mux.HandleFunc("GET /alunos/detalhes", listarAlunosComPlano)
	mux.HandleFunc("GET /alunos/{id}", obterAlunosPorID)
	mux.HandleFunc("PUT /alunos/{id}", atualizarAluno)
	mux.HandleFunc("DELETE /alunos/{id}", deletarAluno)
	mux.HandleFunc("GET /alunos", listarAlunos)

	mux.HandleFunc("GET /plano/{id}/alunos", listarAlunosPorPlano)

	fmt.Println("Servidor Rodando em http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", mux))
}
func criarTabelas() {
	query := `
	PRAGMA foreign_keys = ON;
	CREATE TABLE IF NOT EXISTS planos(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	preco REAL NOT NULL
	);
	CREATE TABLE IF NOT EXISTS alunos(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	email TEXT NOT NULL,
	plano_id INTEGER NOT NULL,
	FOREIGN KEY(plano_id) REFERENCES planos(id) ON DELETE CASCADE
	);
 

	INSERT INTO planos (id, nome, preco)
	SELECT 1, 'Plano Mensal Standart', 89.90 WHERE NOT EXISTS (SELECT 1 FROM planos WHERE id = 1);

	INSERT INTO planos (id, nome, preco)
	SELECT 2, 'Plano VIP Anual', 149.90 WHERE NOT EXISTS (SELECT 2 FROM planos WHERE id = 2);

	INSERT INTO planos (id, nome, preco)
	SELECT 3, 'Plano Semanal Standart', 25.90 WHERE NOT EXISTS (SELECT 3 FROM planos WHERE id = 3);

	INSERT INTO alunos (id, nome, email, plano_id)
	SELECT 1, 'Mateus Silva', 'mateus@email.com', 1 WHERE NOT EXISTS (SELECT 1 FROM alunos WHERE id = 1);

	INSERT INTO alunos (id, nome, email, plano_id)
	SELECT 2, 'Rononoa Zoro', 'ronin@email.com', 2 WHERE NOT EXISTS (SELECT 1 FROM alunos WHERE id = 2);

	INSERT INTO alunos (id, nome, email, plano_id)
	SELECT 3, 'Carlos Lobato', 'monteirolobato@email.com', 1 WHERE NOT EXISTS (SELECT 1 FROM alunos WHERE id = 3);

	INSERT INTO alunos (id, nome, email, plano_id)
	SELECT 4, 'Diego da Silva', 'diegosilva@email.com', 3 WHERE NOT EXISTS (SELECT 1 FROM alunos WHERE id = 4);
	`

	_, err := db.Exec(query)
	if err != nil {
		log.Fatalf("Erro ao Criar as tabelas %v", err)
	}
}
func responderJSON(w http.ResponseWriter, status int, dados interface{}) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	if dados != nil {
		json.NewEncoder(w).Encode(dados)
	}
}

/*
COISAS DO PAI ///////////////////////////////////////////////
*/
func criarPlano(w http.ResponseWriter, r *http.Request) {
	var p Plano
	if err := json.NewDecoder(r.Body).Decode(&p); err != nil || strings.TrimSpace(p.Nome) == "" {
		responderJSON(w, http.StatusBadRequest, map[string]string{"erro": "Dados inválidos"})
		return
	}
	res, err := db.Exec("INSERT INTO planos (nome, preco) VALUES (?,?)", p.Nome, p.Preco)
	if err != nil {
		responderJSON(w, http.StatusInternalServerError, map[string]string{"erro": err.Error()})
		return
	}

	id, _ := res.LastInsertId()
	p.ID = int(id)
	responderJSON(w, http.StatusCreated, p) // esse é o 201
}

func listarPlano(w http.ResponseWriter, r *http.Request) {
	rows, err := db.Query("SELECT id, nome, preco FROM planos")
	if err != nil {
		responderJSON(w, http.StatusInternalServerError, map[string]string{"erro": err.Error()})
		return
	}

	defer rows.Close()

	planos := []Plano{}
	for rows.Next() {
		var p Plano
		rows.Scan(&p.ID, &p.Nome, &p.Preco)
		planos = append(planos, p)
	}
	responderJSON(w, http.StatusOK, planos)
}

/*
	COISAS DO FI AGORA ///////////////////////////////////////
*/

// pequena coisa pra um /alunos funcionar e mostrar todo mundo
func listarAlunos(w http.ResponseWriter, r *http.Request) {
	rows, err := db.Query("SELECT id, Nome, Email, Plano_id FROM alunos")
	if err != nil {
		responderJSON(w, http.StatusInternalServerError, map[string]string{"erro": err.Error()})
		return
	}
	defer rows.Close()

	alunos := []Aluno{}
	for rows.Next() {
		var a Aluno
		rows.Scan(&a.ID, &a.Nome, &a.Email, &a.PlanoID)
		alunos = append(alunos, a)
	}
	responderJSON(w, http.StatusOK, alunos)
}

// CRIATE- C
func criarAluno(w http.ResponseWriter, r *http.Request) {
	var a Aluno
	if err := json.NewDecoder(r.Body).Decode(&a); err != nil || a.PlanoID <= 0 || strings.TrimSpace(a.Nome) == "" {
		responderJSON(w, http.StatusBadRequest, map[string]string{"erro": "dados do alunio invalido"})
		return
	}

	res, err := db.Exec("INSERT INTO alunos (nome, email, plano_id) VALUES (?, ?, ?)", a.Nome, a.Email, a.PlanoID)
	if err != nil {
		responderJSON(w, http.StatusBadRequest, map[string]string{"erro": "Erro ao criar aluno Verifique se o plano do ID existe"})
		return
	}

	id, _ := res.LastInsertId()
	a.ID = int(id)
	responderJSON(w, http.StatusCreated, a) // 2 0 1

}

// LER Lesão por escrivao reposicionado "Obrigado Celia kout cabral vulgo ada lovelanche"
// READ D
func obterAlunosPorID(w http.ResponseWriter, r *http.Request) {
	idStr := r.PathValue("id")
	id, _ := strconv.Atoi(idStr)

	var a Aluno
	err := db.QueryRow("SELECT id, nome, email, plano_id FROM alunos WHERE id = ?", id).
		Scan(&a.ID, &a.Nome, &a.Email, &a.PlanoID)

	if err == sql.ErrNoRows {
		responderJSON(w, http.StatusNotFound, map[string]string{"erro": "Erro Aluno não encontrado"}) // 4 0 4
		return
	} else if err != nil {
		responderJSON(w, http.StatusInternalServerError, map[string]string{"erro": err.Error()})
		return
	}
	responderJSON(w, http.StatusOK, a)
}

// UPDATE U
func atualizarAluno(w http.ResponseWriter, r *http.Request) {
	idStr := r.PathValue("id")
	id, _ := strconv.Atoi(idStr)

	var a Aluno
	if err := json.NewDecoder(r.Body).Decode(&a); err != nil || strings.TrimSpace(a.Nome) == "" {
		responderJSON(w, http.StatusBadRequest, map[string]string{"erro": "Dados inválidos para atualização"})
		return
	}
	res, err := db.Exec("UPDATE alunos SET nome = ?,email = ?, plano_id = ? WHERE id = ?", a.Nome, a.Email, a.PlanoID, id)
	if err != nil {
		responderJSON(w, http.StatusBadRequest, map[string]string{"erro": err.Error()})
		return
	}
	linhasAfetadas, _ := res.RowsAffected()
	if linhasAfetadas == 0 {
		responderJSON(w, http.StatusNotFound, map[string]string{"erro": "Erro não encontrado"})
		return
	}

	a.ID = id
	responderJSON(w, http.StatusOK, a)
}

// Sem a IA eu não faria a isso mas também eu sei o que eu to fazendo??
// Parcialmente quanto mais eu escrevo na mão eu entendo o que eu faço aqui
// PROF DIEGO MELHOR DO PANARÁ
// DELETE D
func deletarAluno(w http.ResponseWriter, r *http.Request) {
	idStr := r.PathValue("id")
	id, _ := strconv.Atoi(idStr)

	res, err := db.Exec("DELETE FROM alunos WHERE id = ?", id)

	if err != nil {
		responderJSON(w, http.StatusInternalServerError, map[string]string{"erro": err.Error()})
		return
	}

	linhasAfetadas, _ := res.RowsAffected()
	if linhasAfetadas == 0 {
		responderJSON(w, http.StatusNotFound, map[string]string{"erro": err.Error()})
		return
	}

	responderJSON(w, http.StatusNoContent, nil) // sucesso porém sem the corpse
}

// CRUD Teóricamente está completo ===============================================================
// Algumas rotas join e o krl ai
// 1. ROTA COM JOIN: traz o nome do pai junto com o filho
func listarAlunosComPlano(w http.ResponseWriter, r *http.Request) {
	query := `
	SELECT a.id, a.nome, a.email, a.plano_id, p.nome
	FROM alunos a
	INNER JOIN planos p ON a.plano_id = p.id
	`
	rows, err := db.Query(query)

	if err != nil {
		responderJSON(w, http.StatusInternalServerError, map[string]string{"erro": err.Error()})
		return
	}
	defer rows.Close()

	alunos := []Aluno{}
	for rows.Next() {
		var a Aluno
		rows.Scan(&a.ID, &a.Nome, &a.Email, &a.PlanoID, &a.NomePlano)
		alunos = append(alunos, a)
	}
	responderJSON(w, http.StatusOK, alunos)
}

// 2. FILTRO POR CAMINHO: traz os filhos de um pai
func listarAlunosPorPlano(w http.ResponseWriter, r *http.Request) {
	planoIDStr := r.PathValue("id")
	planoID, _ := strconv.Atoi(planoIDStr)

	rows, err := db.Query("SELECT id, nome, email, plano_id FROM alunos WHERE plano_id = ?", planoID)
	if err != nil {
		responderJSON(w, http.StatusInternalServerError, map[string]string{"erro": err.Error()})
		return
	}
	defer rows.Close()

	alunos := []Aluno{}
	for rows.Next() {
		var a Aluno
		rows.Scan(&a.ID, &a.Nome, &a.Email, &a.PlanoID)
		alunos = append(alunos, a)
	}
	responderJSON(w, http.StatusOK, alunos)
}

// 3. BUSCA POR QUERY STRING COM LIKE
func buscarAlunosPorNome(w http.ResponseWriter, r *http.Request) {
	nomeBusca := r.URL.Query().Get("nome")
	if nomeBusca == "" {
		responderJSON(w, http.StatusBadRequest, map[string]string{"erro": "Erro, informe o nome"})
		return
	}
	query := "SELECT id, nome, email, plano_id FROM alunos WHERE nome LIKE ?"
	rows, err := db.Query(query, "%"+nomeBusca+"%")
	if err != nil {
		responderJSON(w, http.StatusInternalServerError, map[string]string{"erro": err.Error()})
		return
	}
	defer rows.Close()

	alunos := []Aluno{}
	for rows.Next() {
		var a Aluno
		rows.Scan(&a.ID, &a.Nome, &a.Email, &a.PlanoID)
		alunos = append(alunos, a)
	}
	responderJSON(w, http.StatusOK, alunos)
}
