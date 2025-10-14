from Cifrado import Cifrado
from Descifrado import Descifrado
from Key import Key


def menu():
    print("Cifrado: Matriz de Hill")
    text = input("Ingresa el mensaje a cifrar: ")
    textoClaro = text.upper()
    print("Mensaje a cifrar: ", textoClaro)
    cifrado = Cifrado(textoClaro)
    numeros = []
    for c in textoClaro:
        if c == " ":
            numeros.append(26)
        else:
            numeros.append(ord(c) - ord('A'))

    print("Valores numéricos:", numeros)

    print(len(numeros))
    
    n = 1

    while len(numeros)%n != 0:
        print(n)
        if len(numeros)%n != 0:
            if n*n < len(numeros):
                n += 1
            elif n*n > len(numeros):
                while len(numeros) % n != 0:
                    numeros.append(26)

    print(len(numeros))

if __name__ == "__main__":
    menu()
    