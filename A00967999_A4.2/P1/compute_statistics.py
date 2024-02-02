"""Programa para obtener valores estadísticos de un archivo dado."""

import sys
import time

class StatisticsCalculator:
    """Clase que genera una Calculadora de valores estadísticos."""
    def __init__(self, filename):
        self.filename = filename
        self.data = self.leer_datos()
        self.stats = {}

    def leer_datos(self):
        """Funcion para leer los datos de un archivo."""
        datos = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    try:
                        num = float(line.strip())
                        datos.append(num)
                    except ValueError:
                        print(f"Dato inválido encontrado: {line.strip()}")

        except FileNotFoundError:
            print("Archivo no encontrado.")
            sys.exit(1)

        return datos

    def calcular_media(self):
        """Funcion para calcular la media / promedio."""
        return sum(self.data) / len(self.data)

    def calcular_mediana(self):
        """Funcion para la mediana."""
        datos_ordenados = sorted(self.data)
        n_data = len(datos_ordenados)
        if n_data % 2 == 0:
            return (datos_ordenados[n_data//2 - 1] + datos_ordenados[n_data//2]) / 2
        return datos_ordenados[n_data//2]

    def calcular_moda(self):
        """Funcion para la moda."""
        frecuencia = {}
        for num in self.data:
            frecuencia[num] = frecuencia.get(num, 0) + 1

        moda = max(frecuencia, key=frecuencia.get)
        return moda

    def calcular_varianza(self):
        """Funcion para calcular la varianza."""
        media = self.calcular_media()
        sumatoria_cuadrados_diferencias = 0
        for dato in self.data:
            diferencia = dato - media
            sumatoria_cuadrados_diferencias += diferencia * diferencia
        varianza = sumatoria_cuadrados_diferencias / (len(self.data) - 1)
        return varianza


    def calcular_desviacion_estandar(self):
        """Funcion para calcular la desviación estándar."""
        varianza = self.calcular_varianza()
        return varianza ** 0.5

    def contar_numeros_validos(self):
        """Funcion para contar los números válidos."""
        return len(self.data)

    def calcular_estadisticas(self):
        """Funcion para calcular todas las métricas estadísticas."""
        start_time = time.time()

        self.stats['Media'] = self.calcular_media()
        self.stats['Mediana'] = self.calcular_mediana()
        self.stats['Moda'] = self.calcular_moda()
        self.stats['Varianza'] = self.calcular_varianza()
        self.stats['Desviación Estándar'] = self.calcular_desviacion_estandar()
        self.stats['Cantidad de Números Válidos'] = self.contar_numeros_validos()

        end_time = time.time()
        elapsed_time = end_time - start_time
        self.stats['Tiempo Transcurrido'] = elapsed_time

    def imprimir_estadisticas(self):
        """Funcion para imprimir en pantalla los valores."""
        for estadistica, valor in self.stats.items():
            print(f"{estadistica}: {valor}")

    def escribir_a_archivo(self):
        """Funcion para grabar los datos en un archivo."""
        with open('resultados_estadisticos.txt', 'w', encoding='utf-8') as archivo_abierto:
            archivo_abierto.write("Estadísticas Descriptivas\n")
            archivo_abierto.write("------------------------\n")
            for estadistica, valor in self.stats.items():
                archivo_abierto.write(f"{estadistica}: {valor}\n")


if __name__ == "__main__":
    #MAIN
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    FILENAME_FINAL = sys.argv[1]
    calculator = StatisticsCalculator(FILENAME_FINAL)
    calculator.calcular_estadisticas()
    calculator.imprimir_estadisticas()
    calculator.escribir_a_archivo()
