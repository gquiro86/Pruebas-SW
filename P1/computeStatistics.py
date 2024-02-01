import sys
import time

class StatisticsCalculator:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.leer_datos()
        self.stats = {}

    def leer_datos(self):
        datos = []
        try:
            with open(self.filename, 'r') as file:
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
        return sum(self.data) / len(self.data)

    def calcular_mediana(self):
        datos_ordenados = sorted(self.data)
        n = len(datos_ordenados)
        if n % 2 == 0:
            return (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
        else:
            return datos_ordenados[n//2]

    def calcular_moda(self):
        frecuencia = {}
        for num in self.data:
            frecuencia[num] = frecuencia.get(num, 0) + 1

        moda = max(frecuencia, key=frecuencia.get)
        return moda

    def calcular_varianza(self):
        media = self.calcular_media()
        varianza = sum((x - media) ** 2 for x in self.data) / len(self.data)
        return varianza

    def calcular_desviacion_estandar(self):
        varianza = self.calcular_varianza()
        return varianza ** 0.5

    def contar_numeros_validos(self):
        return len(self.data)

    def calcular_estadisticas(self):
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
        for estadistica, valor in self.stats.items():
            print(f"{estadistica}: {valor}")

    def escribir_a_archivo(self):
        with open('ResultadosEstadisticos.txt', 'w') as f:
            f.write("Estadísticas Descriptivas\n")
            f.write("------------------------\n")
            for estadistica, valor in self.stats.items():
                f.write(f"{estadistica}: {valor}\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    calculator = StatisticsCalculator(filename)
    calculator.calcular_estadisticas()
    calculator.imprimir_estadisticas()
    calculator.escribir_a_archivo()
