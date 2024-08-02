vendas = {
    "Camisa": 1500,
    "Calça": 1450,
    "Camiseta": 1750,
    "Moletom": 1200,
    "Boné": 1750,
    "Tênis": 1300,
    "Chinelo": 1000
}

maior_quantidade = max(vendas.values())
produtos_mais_vendidos = [produto for produto, quantidade in vendas.items() if quantidade == maior_quantidade]

print(f"Produto(s) mais vendido(s): {produtos_mais_vendidos} (quantidade: {maior_quantidade})")