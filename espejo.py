
def reflejar_texto(texto):
    texto_reflejado = ""
    for i in range(len(texto) - 1, -1, -1):
        texto_reflejado += texto[i]
    return texto_reflejado

if __name__ == "__main__":
    texto_usuario = input("Introduce el texto que quieres reflejar: ")
    texto_reflejado = reflejar_texto(texto_usuario)
    print("Texto reflejado: ", texto_reflejado)