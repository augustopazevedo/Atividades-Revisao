def eh_palindromo(palavra):
    palavra_filtrada = ''.join(c for c in palavra if c.isalnum()).lower()
    return palavra_filtrada == palavra_filtrada[::-1]

def encontrar_palindromos(palavras):

    palindromos = []
    for palavra in palavras:
        if eh_palindromo(palavra):
            palindromos.append(palavra)
    return palindromos

palavras = ["Radar", "Casa", "Escola", "Arara", "Osso", "Amor", "Reviver"]
resultado = encontrar_palindromos(palavras)
print(resultado) 