class DescifradoH:
    def __init__(self):
        self.modulo = 27
    
    def conversion(self, mensaje_cifrado):
        #convierte el mensaje cifrado a valores numéricos usando la misma lógica que Cifrado.py
        numeros = []
        for c in mensaje_cifrado:
            if c == " ": 
                numeros.append(26)
            else:
                numeros.append(ord(c) - ord('A'))
        return numeros
    
    def div_bloques(self, numeros, n):
        #divide los números en bloques del tamaño de la matriz clave
        bloques = []
        for i in range(0, len(numeros), n):
            bloque = numeros[i:i+n]
            bloques.append(bloque)
        return bloques
    
    def calcular_determinante(self, matriz):
        #calcula el determinante de una matriz cuadrada
        n = len(matriz)
        
        if n == 1:
            return matriz[0][0]
        elif n == 2:
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        else:
            det = 0
            for c in range(n):
                submatriz = [fila[:c] + fila[c+1:] for fila in matriz[1:]]
                det += ((-1) ** c) * matriz[0][c] * self.calcular_determinante(submatriz)
            return det
    
    def calcular_matriz_adjunta(self, matriz):
        #calcula la matriz adjunta (matriz de cofactores)
        n = len(matriz)
        adjunta = []
        
        for i in range(n):
            fila = []
            for j in range(n):
                #crear submatriz eliminando fila i y columna j
                submatriz = []
                for k in range(n):
                    if k != i:
                        fila_sub = []
                        for l in range(n):
                            if l != j:
                                fila_sub.append(matriz[k][l])
                        submatriz.append(fila_sub)
                
                #calcular cofactor
                cofactor = ((-1) ** (i + j)) * self.calcular_determinante(submatriz)
                fila.append(cofactor)
            adjunta.append(fila)
        
        return adjunta
    
    def transponer_matriz(self, matriz):
        #calcula la transpuesta de una matriz
        n = len(matriz)
        m = len(matriz[0])
        transpuesta = []
        
        for j in range(m):
            fila = []
            for i in range(n):
                fila.append(matriz[i][j])
            transpuesta.append(fila)
        
        return transpuesta
    
    def calcular_inversa_multiplicativa(self, det, modulo):
        #calcula el inverso multiplicativo usando el algoritmo extendido de Euclides
        def gcd_extendido(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = gcd_extendido(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
        
        gcd, x, y = gcd_extendido(det, modulo)
        if gcd != 1:
            raise ValueError(f"No existe inverso multiplicativo para {det} módulo {modulo}")
        
        return x % modulo
    
    def calcular_matriz_inversa(self, matriz_clave):
        """
        Calcula la matriz inversa siguiendo los pasos:
        1. Calcular determinante |A|
        2. Calcular adjunta Adj(A)
        3. Obtener transpuesta Adj(Aᵗ)
        4. Aplicar A⁻¹ = (1/|A|) * Adj(Aᵗ)
        """
        #1: Calcular determinante
        det = self.calcular_determinante(matriz_clave)
        
        # Aplicar módulo al determinante para trabajar en Z27
        det_mod = det % self.modulo
        
        #2: Calcular matriz adjunta
        adjunta = self.calcular_matriz_adjunta(matriz_clave)
        
        #3: Obtener transpuesta de la adjunta
        adjunta_transpuesta = self.transponer_matriz(adjunta)
        
        #4: Calcular inversa multiplicativa del determinante (en módulo)
        det_inverso = self.calcular_inversa_multiplicativa(det_mod, self.modulo)
        
        #5: Aplicar A⁻¹ = (1/|A|) * Adj(Aᵗ)
        n = len(matriz_clave)
        inversa = []
        for i in range(n):
            fila = []
            for j in range(n):
                elemento = det_inverso * adjunta_transpuesta[i][j]
                fila.append(elemento)
            inversa.append(fila)
        
        return inversa
    
    def aplicar_modulo_27(self, matriz):
        #aplica módulo 27 a todos los elementos de la matriz
        resultado = []
        for i in range(len(matriz)):
            fila = []
            for j in range(len(matriz[i])):
                elemento_mod = matriz[i][j] % self.modulo
                fila.append(elemento_mod)
            resultado.append(fila)
        
        return resultado
    
    def multiplicar_matriz_por_bloques(self, matriz_inversa, bloques_mensaje):
        #multiplica la matriz inversa por cada bloque del mensaje
        bloques_resultado = []
        
        for bloque in bloques_mensaje:
            bloque_resultado = []
            
            for fila in matriz_inversa:
                suma = 0
                for j in range(len(bloque)):
                    suma += fila[j] * bloque[j]
                bloque_resultado.append(suma)
            
            bloques_resultado.append(bloque_resultado)
        
        return bloques_resultado
    
    def aplicar_modulo_27_bloques(self, bloques):
        #aplica módulo 27 a todos los elementos de los bloques
        bloques_mod = []
        
        for bloque in bloques:
            bloque_mod = [elemento % self.modulo for elemento in bloque]
            bloques_mod.append(bloque_mod)
        
        return bloques_mod
    
    def matriz_a_vector(self, bloques):
        
        #convierte los bloques de matriz en un vector único
        vector = []
        for bloque in bloques:
            vector.extend(bloque)
        return vector
    
    def conversion_inversa(self, bloques):
        #convierte los números descifrados de vuelta a texto usando la misma lógica que Cifrado.py
        texto = ""
        for bloque in bloques:
            for num in bloque:
                if num == 26:
                    texto += " "
                elif 0 <= num <= 25:
                    texto += chr(num + ord('A'))
        return texto
    
    def descifrar_mensaje(self, mensaje_cifrado, matriz_clave):
        #función principal que ejecuta todo el algoritmo de descifrado
        
        #obtener el mensaje cifrado, asignarle valor numérico y convertirlo en matriz
        valores_numericos = self.conversion(mensaje_cifrado)
        tamano_matriz = len(matriz_clave)
        bloques_mensaje = self.div_bloques(valores_numericos, tamano_matriz)
        
        #1. Calcular la inversa de la matriz clave
        # a) Calcular la determinante |A|
        # b) Calcular la adjunta Adj(A)
        # c) Obtener la traspuesta de esa adjunta Adj(Aᵗ)
        #2. Al final aplicar A⁻¹ = (1 / |A|) * Adj(Aᵗ)
        matriz_inversa = self.calcular_matriz_inversa(matriz_clave)
        
        #3. Después a esa inversa aplicar el mod 27
        matriz_inversa_mod = self.aplicar_modulo_27(matriz_inversa)
        
        #4. Después multiplicar el resultado de paso 3 por la matriz del mensaje
        bloques_multiplicados = self.multiplicar_matriz_por_bloques(matriz_inversa_mod, bloques_mensaje)
        
        #5. Aplicarle de nuevo el modulo 27 al resultado del paso 4
        bloques_mod = self.aplicar_modulo_27_bloques(bloques_multiplicados)
        
        #6. Reescribir la matriz en vector y asignarle un carácter de acuerdo al alfabeto
        mensaje_descifrado = self.conversion_inversa(bloques_mod)
        
        return mensaje_descifrado