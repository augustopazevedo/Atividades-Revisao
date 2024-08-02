def cores_longas(cores):
    return {cor for cor in cores if len(cor) > 4}

cores = {"Amarelo", "Roxo", "Azul", "Vermelho", "Rosa", "Laranja"}
resultado = cores_longas(cores)
print(resultado)