

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
            numeros.extend([27] * padding_needed)
            print(f"Se añadieron {padding_needed} caracteres de padding (27)")
        
        print(f"Longitud después del padding: {len(numeros)}")
        print("Valores numéricos con padding:", numeros)

        return numeros

    def div_bloques(self, numeros, bloques, n):
        for i in range(0, len(numeros), n):
            bloque = numeros[i:i+n]
            bloques.append(bloque)
        return bloques