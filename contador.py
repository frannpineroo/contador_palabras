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

archivo = input("Ingrese la ruta del archivo de texto: ")
try:
    with open(archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
except FileNotFoundError:
    print(f"El archivo {archivo} no existe")
    exit(1)

# Separar el texto en palabras

palabras = re.findall(r'\b\w+\b', texto.lower())
total_palabras = len(palabras)
print(f"Total de palabras: {total_palabras}")

contador = Counter(palabras)
mas_comunes = contador.most_common(10)
print("Palabras más comunes:")
for palabra, freq in mas_comunes:
    print(f"{palabra}: {freq}")