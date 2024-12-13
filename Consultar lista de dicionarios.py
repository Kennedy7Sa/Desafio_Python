pessoas = [
    {"nome": "Kennedy", "peso": 69.55, "id": 1, "tamanho": 1.75},
    {"nome": "Sara", "peso": 65.55, "id": 2, "tamanho": 1.65},
    {"nome": "Laura", "peso": 16.85, "id": 3, "tamanho": 1.00}
]

# Solicita o valor a ser pesquisado
valor_pesquisa = input("Digite o valor a ser pesquisado (ou 'todos' para exibir tudo): ").strip().lower()

# Busca registros na lista
def buscar_registros(lista_pessoas, valor):
    # Se o usuário digitar 'todos', retorna toda a lista
    if valor == "todos" or valor == "all":
        return lista_pessoas

    # Caso contrário, busca pelo valor nos registros
    return [
        pessoa for pessoa in lista_pessoas
        if any(str(v).lower() == valor for v in pessoa.values())
    ]

# Executa a busca e exibe os resultados
resultados = buscar_registros(pessoas, valor_pesquisa)

if resultados:
    print("\nRegistro(s) encontrado(s):")
    for resultado in resultados:
        for chave, valor in resultado.items():
            print(f"{chave}: {valor}")
        print("-" * 20)  
else:
    print("\nNenhum registro encontrado com o valor especificado.")
