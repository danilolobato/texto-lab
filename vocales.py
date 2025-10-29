
def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    cantidad = contar_vocales(texto)
    print(f"El texto contiene {cantidad} vocal(es).")