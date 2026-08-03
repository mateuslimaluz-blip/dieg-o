package main

import (
	"encoding/json"
	"net/http"
)

type resposta struct {
	Mensagem string `json:"mensagem"`
}

func main() {
	mux := http.NewServeMux()

	mux.HandleFunc("GET /api/Mensagem", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")

		dados := resposta{Mensagem: "Olá acho que vai funcionar"}

		json.NewEncoder(w).Encode(dados)
	})

	println("Servidor rodando em local:8080 YIPPE")
	http.ListenAndServe(":8080", mux)
}