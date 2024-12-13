# 📜 Pesquisa de Registros - Busca Simples

Esse script permite buscar registros de pessoas dentro de uma lista de dicionários, onde você pode procurar por nome, peso, tamanho ou qualquer outro valor. É uma forma simples e rápida de filtrar informações de uma maneira eficiente.

---

## 🚀 Funcionalidade

O código recebe um valor de pesquisa e retorna os registros de pessoas que correspondem ao critério. Caso o valor inserido seja "todos" ou "all", todos os registros serão exibidos.

---

## 📝 Exemplo de Dados

A lista de pessoas contém informações sobre:

- **Nome**
- **Peso**
- **ID**
- **Tamanho (altura)**

Exemplo de dados carregados:

```python
pessoas = [
    {"nome": "Kennedy", "peso": 69.55, "id": 1, "tamanho": 1.75},
    {"nome": "Sara", "peso": 65.55, "id": 2, "tamanho": 1.65},
    {"nome": "Laura", "peso": 16.85, "id": 3, "tamanho": 1.00}
]
Digite o valor a ser pesquisado (ou 'todos' para exibir tudo): kennedy

Registro(s) encontrado(s):
nome: Kennedy
peso: 69.55
id: 1
tamanho: 1.75
--------------------


