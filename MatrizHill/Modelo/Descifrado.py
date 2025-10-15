
#para el descifrado del mensje cifrado el procedimieto es el siguiente:
#1. calcular la matriz inversa de la matriz clave modulo 27
#2. multiplicar cada bloque del mensaje cifrado por la matriz inversa modulo 27
#3. convertir los numeros resultantes a caracteres
#4. eliminar los caracteres de padding (26) si es necesario

#nota: la matriz clave debe ser invertible modulo 27 para que el descifrado sea posible

class Descifrado:
    def __init__(self):
        pass
    
    def calcular_inversa_modulo(self, matriz, modulo=27):
        """
        Calcula la matriz inversa módulo 27 usando el método de adjuntos
        """
        n = len(matriz)
        
        det = self.determinante(matriz) % modulo
        
        #inverso multiplicativo del determinante
        det_inverso = self.inverso_multiplicativo(det, modulo)
        
        #matriz adjunta
        adjunta = self.matriz_adjunta(matriz)
        
        #matriz inversa: (det_inverso * adjunta) mod modulo
        inversa = []
        for i in range(n):
            fila = []
            for j in range(n):
                elemento = (det_inverso * adjunta[i][j]) % modulo
                fila.append(elemento)
            inversa.append(fila)
        
        return inversa
    
    def determinante(self, matriz):
        """
        Calcula el determinante de una matriz cuadrada
        """
        n = len(matriz)
        if n == 1:
            return matriz[0][0]
        elif n == 2:
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        else:
            det = 0
            for c in range(n):
                submatriz = [fila[:c] + fila[c+1:] for fila in matriz[1:]]
                det += ((-1) ** c) * matriz[0][c] * self.determinante(submatriz)
            return det
    
    def matriz_adjunta(self, matriz):
        """
        Calcula la matriz adjunta (transpuesta de la matriz de cofactores)
        """
        n = len(matriz)
        adjunta = []
        
        for i in range(n):
            fila = []
            for j in range(n):
                #submatriz eliminando fila i y columna j
                submatriz = []
                for k in range(n):
                    if k != i:
                        fila_sub = []
                        for l in range(n):
                            if l != j:
                                fila_sub.append(matriz[k][l])
                        submatriz.append(fila_sub)
                
                #calcular cofactor
                cofactor = ((-1) ** (i + j)) * self.determinante(submatriz)
                fila.append(cofactor)
            adjunta.append(fila)
        
        #transponer la matriz de cofactores para obtener la adjunta
        adjunta_transpuesta = []
        for j in range(n):
            fila = []
            for i in range(n):
                fila.append(adjunta[i][j])
            adjunta_transpuesta.append(fila)
        
        return adjunta_transpuesta
    
    def inverso_multiplicativo(self, a, m):
        """
        Calcula el inverso multiplicativo de 'a' módulo 'm' usando el algoritmo extendido de Euclides
        """
        def gcd_extendido(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = gcd_extendido(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
        
        gcd, x, y = gcd_extendido(a, m)
        if gcd != 1:
            raise ValueError(f"No existe inverso multiplicativo para {a} módulo {m}")
        
        return x % m
    
    def multiplicar_matriz_vector(self, matriz, vector):
        """
        Multiplica una matriz por un vector y aplica módulo 27
        """
        resultado = []
        for i in range(len(matriz)):
            suma = 0
            for j in range(len(vector)):
                suma += matriz[i][j] * vector[j]
            resultado.append(suma % 27)
        return resultado
    
    def descifrar_bloques(self, bloques_cifrados, matriz_clave):
        """
        Descifra los bloques usando la matriz inversa
        """
        #calcular matriz inversa
        matriz_inversa = self.calcular_inversa_modulo(matriz_clave)
        
        print("\nMatriz inversa:")
        for fila in matriz_inversa:
            print(fila)
        
        bloques_descifrados = []
        for bloque in bloques_cifrados:
            bloque_descifrado = self.multiplicar_matriz_vector(matriz_inversa, bloque)
            bloques_descifrados.append(bloque_descifrado)
        
        return bloques_descifrados
    
    def conversion_inversa(self, bloques):
        """
        Convierte los números descifrados de vuelta a texto
        """
        texto = ""
        for bloque in bloques:
            for num in bloque:
                if num == 26:
                    texto += " "
                elif 0 <= num <= 25:
                    texto += chr(num + ord('A'))
        return texto
    
    def eliminar_padding(self, texto):
        """
        Elimina los caracteres de padding (espacios al final) que se añadieron durante el cifrado
        """
        #eliminar espacios al final que fueron añadidos como padding
        return texto.rstrip()
    