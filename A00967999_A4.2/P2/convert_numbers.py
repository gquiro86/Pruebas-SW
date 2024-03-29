"""Programa para convertir números decimales a binarios y Hexadecimales."""

import sys
import time


def convertir_a_binario(decimal):
    """Convierte un número decimal a binario."""
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario


def convertir_a_hexadecimal(decimal):
    """Convierte un número decimal a hexadecimal."""
    caracteres_hex = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        hexadecimal = caracteres_hex[residuo] + hexadecimal
        decimal //= 16
    return hexadecimal


def procesar_archivo(nombre_archivo_procesar):
    """Procesa el archivo que contiene números."""
    tiempo_inicio = time.time()
    try:
        with open(nombre_archivo_procesar, 'r',encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                try:
                    numero = int(linea.strip())
                    binario = convertir_a_binario(numero)
                    hexadecimal = convertir_a_hexadecimal(numero)
                    print(f"Decimal: {numero}, Binario: {binario}, Hexadecimal: {hexadecimal}")
                    with open("resultados_conv.txt", 'a',encoding='utf-8') as archivo_resultados:
                        archivo_resultados.write(f"Decimal: {numero}, Binario: {binario}, "
                         f"Hexadecimal: {hexadecimal}\n")
                except ValueError:
                    print(f"Error: Datos inválidos encontrados en el archivo: {linea.strip()}")

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")

    tiempo_fin = time.time()
    tiempo_transcurrido = tiempo_fin - tiempo_inicio
    print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")
    with open("resultados_conv.txt", 'a',encoding='utf-8') as archivo_resultados:
        archivo_resultados.write(f"Tiempo transcurrido: {tiempo_transcurrido} segundos\n")


if __name__ == "__main__":
    #MAIN
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py archivo_con_datos.txt")
    else:
        NOMBRE_ARCHIVO = sys.argv[1]
        procesar_archivo(NOMBRE_ARCHIVO)
