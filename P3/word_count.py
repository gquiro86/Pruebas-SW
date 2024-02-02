"""Module providing a method to count words from a given file in .txt."""

import sys
import time

def contar_palabras(archivo):
    """
    Cuenta las palabras en un archivo y devuelve un diccionario con las frecuencias.
    """
    conteo_palabras = {}
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            for linea in file:
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


def imprimir_y_escribir_resultados(conteo_palabras_imprimir,tiempo_transcurrido_imprimir):
    """
    Se adiciona el texto en el archivo de salida.
    """
    palabras_ordenadas = sorted(conteo_palabras_imprimir.items(), key=lambda x: x[0])
    with open('WordCountResults.txt', 'w', encoding='utf-8') as archivo_resultado:
        archivo_resultado.write("Palabra\tFrecuencia\n")
        for palabra, frecuencia in palabras_ordenadas:
            archivo_resultado.write(f"{palabra}\t{frecuencia}\n")

    print("Palabra\tFrecuencia")
    for palabra, frecuencia in palabras_ordenadas:
        print(f"{palabra}\t{frecuencia}")

    print(f"\nTiempo transcurrido: {tiempo_transcurrido_imprimir:.6f} segundos")

if __name__ == "__main__":
    #MAIN
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py archivoConDatos.txt")
    else:
        tiempo_inicio = time.time()
        NOMBRE_ARCHIVO = sys.argv[1]
        conteo_palabras_final = contar_palabras(NOMBRE_ARCHIVO)
        tiempo_fin = time.time()
        tiempo_transcurrido = tiempo_fin - tiempo_inicio
        imprimir_y_escribir_resultados(conteo_palabras_final, tiempo_transcurrido)
