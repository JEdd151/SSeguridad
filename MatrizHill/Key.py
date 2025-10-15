from math import gcd #MCD

class Key:
    def __init__(self, n):
        self.n = n
        self.matriz = self.generar_matriz()
        self.validar_matriz()
    
    def generar_matriz(self):
        print(f"\nIngresa los elementos de la matriz clave {self.n}x{self.n}:")
        matriz = []
        for i in range(self.n):
            fila = []
            for j in range(self.n):
                while True:
                    try:
                        elemento = int(input(f"Elemento [{i+1},{j+1}]: "))
                        fila.append(elemento)
                        break
                    except ValueError:
                        print("Ingresa un numero valido")
            matriz.append(fila)
        return matriz
    
    def determinante (self, matriz):
        n = len (matriz)
        if n == 2:
            return matriz [0][0] * matriz[1][1] - matriz [0][1] * matriz[1][0]
        det = 0

        for c in range(n):
            submatriz = [fila[:c] + fila[c + 1:] for fila in matriz [1:]]
            det += ((-1) ** c) * matriz[0][c] * self.determinante(submatriz)
        return det
    
    def validar_matriz(self):
        det = self.determinante(self.matriz) % 27
        if gcd(det, 27) != 1:
            print (f"\nDeterminante = {det} ¡¡NO INVERTIBLE!!")
            print ("Ingresa otra matriz")
            exit()
        else:
            print(f"\nDeterminante = {det} ¡¡MATRIZ VALIDA!!")


    def mostrar_matriz(self):
        print("\nMatriz clave:")
        for fila in self.matriz:
            print(fila)