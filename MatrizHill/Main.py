from Cifrado import Cifrado
from Descifrado import Descifrado
from Key import Key

def menu():
    print("Cifrado: Matriz de Hill")
    text = input("Ingresa el mensaje a cifrar: ")
    textoClaro = text.upper()
    
    while True:
        try:
            n = int(input("Ingresa el tamaño de bloque n (≥ 2): "))
            if n >= 2:
                break
            else:
                print("El tamaño debe ser ≥ 2")
        except ValueError:
            print("Ingresa un número válido")
    
    print(f"Mensaje a cifrar: {textoClaro}")
    print(f"Usando bloques de tamaño: {n}")

    numeros = []
    
    for c in textoClaro:
        if c == " ":
            numeros.append(26)
        else:
            numeros.append(ord(c) - ord('A'))

    print("Valores numéricos:", numeros)
    print(f"Longitud original: {len(numeros)}")
    
    if len(numeros) % n != 0:
        padding_needed = n - (len(numeros) % n)
        numeros.extend([27] * padding_needed)
        print(f"Se añadieron {padding_needed} caracteres de padding (27)")
    
    print(f"Longitud después del padding: {len(numeros)}")
    print("Valores numéricos con padding:", numeros)

    bloques = []
    for i in range(0, len(numeros), n):
        bloque = numeros[i:i+n]
        bloques.append(bloque)
    
    print(f"\n{len(bloques)} bloques de tamaño {n}:")
    for i, bloque in enumerate(bloques):
        print(f"Bloque {i+1}: {bloque}")

if __name__ == "__main__":
    menu()