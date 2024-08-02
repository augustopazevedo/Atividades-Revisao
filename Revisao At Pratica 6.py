numeros = [101, 47, 59, 85, 48, 36, 12, 156]

def contar_e_listar_pares_impares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    return pares, impares


pares, impares = contar_e_listar_pares_impares(numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)