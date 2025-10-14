class Key:
    def __init__(self, n):
        self.n = n
        self.matriz = self.generar_matriz()
    
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
                        print("Ingresa un número válido")
            matriz.append(fila)
        return matriz
    
    def mostrar_matriz(self):
        print("\nMatriz clave:")
        for fila in self.matriz:
            print(fila)