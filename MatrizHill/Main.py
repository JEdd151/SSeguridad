from Cifrado import Cifrado
from Descifrado import Descifrado
from Key import Key


def menu():
    print("Cifrado: Matriz de Hill")
    textoClaro = input("Ingresa el mensaje a cifrar: ")
    print("Mensaje a cifrar: ", textoClaro.upper())
    cifrado = Cifrado(textoClaro)

    for c in textoClaro:





if __name__ == "__main__":
    menu()
    