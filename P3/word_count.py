import sys
import time

# Función para leer el archivo y contar las palabras
def contar_palabras(nombre_archivo):
    conteo_palabras = {}
    try:
        with open(nombre_archivo, 'r') as archivo:
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
    except Exception as e:
        print("Se produjo un error al procesar el archivo:", e)

    return conteo_palabras

# Función para imprimir y escribir los resultados en un archivo
def imprimir_y_escribir_resultados(conteo_palabras, tiempo_transcurrido):
    palabras_ordenadas = sorted(conteo_palabras.items(), key=lambda x: x[0])
    with open('resultados_conteo_palabras.txt', 'w') as archivo_resultado:
        archivo_resultado.write("Palabra\tFrecuencia\n")
        for palabra, frecuencia in palabras_ordenadas:
            archivo_resultado.write(f"{palabra}\t{frecuencia}\n")

    print("Palabra\tFrecuencia")
    for palabra, frecuencia in palabras_ordenadas:
        print(f"{palabra}\t{frecuencia}")

    print(f"\nTiempo transcurrido: {tiempo_transcurrido:.6f} segundos")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python word_count .py archivos_con_datos.txt")
    else:
        tiempo_inicio = time.time()
        nombre_archivo = sys.argv[1]
        conteo_palabras = contar_palabras(nombre_archivo)
        tiempo_fin = time.time()
        tiempo_transcurrido = tiempo_fin - tiempo_inicio

        imprimir_y_escribir_resultados(conteo_palabras, tiempo_transcurrido)
