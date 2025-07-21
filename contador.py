""" 
Programa para contar palabras en un archivo de texto
1. Pedir al usuario que ingrese la ruta del archivo de texto
2. Leer el archivo de texto
3. Contar las palabras en el archivo de texto
4. Imprimir el número de palabras en el archivo de texto
5. Mostrar las 10 palabras más repetidas 
"""
import re
from collections import Counter

class ContadorDePalabras:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.texto = ''
        self.palabras = []

    def leer_archivo(self):
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                self.texto = archivo.read()
        except FileNotFoundError:
            print(f"El archivo {self.ruta_archivo} no existe")
            exit(1)

    def contar_palabras(self):
        self.palabras = re.findall(r'\b\w+\b', self.texto.lower())
        total_palabras = len(self.palabras)
        print(f"Total de palabras: {total_palabras}")
        contador = Counter(self.palabras)
        mas_comunes = contador.most_common(10)
        print("Palabras más comunes:")
        for palabra, freq in mas_comunes:
            print(f"{palabra}: {freq}")

if __name__ == "__main__":
    archivo = input("Ingrese la ruta del archivo de texto: ")
    contador = ContadorDePalabras(archivo)
    contador.leer_archivo()
    contador.contar_palabras()