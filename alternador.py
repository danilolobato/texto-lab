def alternar_letras(texto):
    resultado = ""
    for i, letra in enumerate(texto):
        if i % 2 == 0:
            resultado += letra.upper()
        else:
            resultado += letra.lower()
    return resultado

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    print(alternar_letras(texto))