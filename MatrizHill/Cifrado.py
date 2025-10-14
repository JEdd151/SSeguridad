

class Cifrado:
    def __init__(self):
        pass


    def conversion(self, textoClaro, n):
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
            numeros.extend([26] * padding_needed)
            print(f"Se añadieron {padding_needed} caracteres de padding (26)")
        
        print(f"Longitud después del padding: {len(numeros)}")
        print("Valores numéricos con padding:", numeros)

        return numeros

    def div_bloques(self, numeros, bloques, n):
        for i in range(0, len(numeros), n):
            bloque = numeros[i:i+n]
            bloques.append(bloque)
        return bloques

    def cifrar_bloques(self, bloques, matriz_clave):
        bloques_cifrados = []
        
        for bloque in bloques:
            bloque_cifrado = self.multiplicar_matriz_vector(matriz_clave, bloque)
            bloques_cifrados.append(bloque_cifrado)
        
        return bloques_cifrados
    
    def multiplicar_matriz_vector(self, matriz, vector):
        resultado = []
        for i in range(len(matriz)):
            suma = 0
            for j in range(len(vector)):
                suma += matriz[i][j] * vector[j]
            resultado.append(suma % 27)
        return resultado


    def conversion_inversa(self, bloques):
        texto = ""
        for bloque in bloques:
            for num in bloque:
                if num == 26:
                    texto += " "
                elif 0 <= num <= 25:
                    texto += chr(num + ord('A'))
        return texto