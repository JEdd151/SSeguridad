from Cifrado import Cifrado
from Descifrado import Descifrado
from Key import Key

cifrado = Cifrado()

def menu():
    print("Cifrado: Matriz de Hill")
    text = input("Ingresa el mensaje a cifrar: ")
    textoClaro = text.upper()
    numeros = []
    bloques = []


    while True:
        try:
            n = int(input("Ingresa el tamaño de bloque n (≥ 2): "))
            if n >= 2:
                break
            else:
                print("El tamaño debe ser ≥ 2")
        except ValueError:
            print("Ingresa un numero valido")
    
    print(f"Mensaje a cifrar: {textoClaro}")
    print(f"Usando bloques de tamaño: {n}")

    
    numeros = cifrado.conversion(textoClaro,n)
    bloques = cifrado.div_bloques(numeros, bloques, n)

    print(f"\n{len(bloques)} bloques de tamaño {n}:")
    for i, bloque in enumerate(bloques):
        print(f"Bloque {i+1}: {bloque}")
    
    key = Key(n)
    key.mostrar_matriz()

    bloques_cifrados = cifrado.cifrar_bloques(bloques, key.matriz)
    
    print(f"\nBloques cifrados:")
    for i, bloque in enumerate(bloques_cifrados):
        print(f"Bloque {i+1}: {bloque}")

    texto_cifrado = cifrado.conversion_inversa(bloques_cifrados)
    print(f"\nTexto cifrado: {texto_cifrado}")




if __name__ == "__main__":
    menu()