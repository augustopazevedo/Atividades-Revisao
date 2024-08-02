def criar_dicionario_produtos():
  produtos = {
      "Feijão": {"preço": 10, "quantidade": 50},
      "Arroz": {"preço": 15, "quantidade": 32},
      "Carne": {"preço": 30, "quantidade": 80},
      "Ovo": {"preço": 12, "quantidade": 22},
      "Leite": {"preço": 4, "quantidade": 35},
      "Macarrão": {"preço": 6, "quantidade": 49}
  }
  return produtos

def adicionar_produto(produtos, nome, preco, quantidade):
  produtos[nome] = {"preço": preco, "quantidade": quantidade}

def remover_produto(produtos, nome):
  if nome in produtos:
    del produtos[nome]
  else:
    print(f"O produto {nome} não foi encontrado.")

def atualizar_produto(produtos, nome, **kwargs):
  if nome in produtos:
    produtos[nome].update(kwargs)
  else:
    print(f"O produto {nome} não foi encontrado.")

produtos = criar_dicionario_produtos()

adicionar_produto(produtos, "Frango", 25, 10)
remover_produto(produtos, "Ovo")
atualizar_produto(produtos, "Feijão", preço=12)

print(produtos)