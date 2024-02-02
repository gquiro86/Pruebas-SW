"""Module providing a method to count words from a given file in .txt."""

import sys
import time

def contar_palabras(nombre_archivo):
    """
    Cuenta las palabras en un archivo y devuelve un diccionario con las frecuencias.
    """
    conteo_palabras = {}
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras = linea.split()
                for palabra in palabras:
                    palabra = palabra.strip().lower()
                    if palabra:
                        if palabra in conteo_palabras:
                            conteo_palabras[palabra] += 1
                        else:
                            conteo_palabras[palabra] = 1
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    return conteo_palabras

def imprimir_y_escribir_resultados(conteo_palabras, tiempo_transcurrido):
    """
    Se adiciona el texto en el archivo de salida.
    """
    palabras_ordenadas = sorted(conteo_palabras.items(), key=lambda x: x[0])
    with open('WordCountResults.txt', 'w', encoding='utf-8') as archivo_resultado:
        archivo_resultado.write("Palabra\tFrecuencia\n")
        for palabra, frecuencia in palabras_ordenadas:
            archivo_resultado.write(f"{palabra}\t{frecuencia}\n")

    print("Palabra\tFrecuencia")
    for palabra, frecuencia in palabras_ordenadas:
        print(f"{palabra}\t{frecuencia}")

    print(f"\nTiempo transcurrido: {tiempo_transcurrido:.6f} segundos")

if __name__ == "__main__":
    """
    MAIN
    """
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py archivoConDatos.txt")
    else:
        tiempo_inicio = time.time()
        nombre_archivo = sys.argv[1]  # pylint: disable=W0621
        conteo_palabras = contar_palabras(nombre_archivo)  # pylint: disable=W0621
        tiempo_fin = time.time()
        tiempo_transcurrido = tiempo_fin - tiempo_inicio

        imprimir_y_escribir_resultados(conteo_palabras, tiempo_transcurrido)
