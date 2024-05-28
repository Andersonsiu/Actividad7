import concurrent.futures  # Importa el modulo concurrent.futures para paralelismo
import time  
import math  # Importa el modulo math para funciones matemáticas

# Funcion para verificar si un numero es primo
def es_primo(n):
    if n <= 1:  # Si el numero es menor o igual a 1, no es primo
        return False
    if n == 2:  # El numero 2 es primo
        return True
    if n % 2 == 0:  # Si el numero es par y mayor que 2, no es primo
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):  # Itera desde 3 hasta la raiz cuadrada de n
        if n % i == 0:  # Si n es divisible por i, no es primo
            return False
    return True  # Si no se encontraron divisores, es primo

# Funcion para encontrar numeros primos 
def encontrar_primos(rango):
    primos = []  # Inicializa la lista de numeros primos
    for n in rango:  # Itera sobre cada numero en el rango
        if es_primo(n):  # Verifica si el numero es primo
            primos.append(n)  # Si es primo, lo añade a la lista
    return primos  # Devuelve la lista de numeros primos

# Medir el tiempo de ejecucion secuencial
inicio_secuencial = time.time()  # Guarda el tiempo de inicio
rango_numeros = range(10**6, 10**6 + 10000)  # Define el rango de numeros a analizar
primos_secuencial = encontrar_primos(rango_numeros)  # Encuentra primos de forma secuencial
fin_secuencial = time.time()  # Guarda el tiempo de finalizacion
tiempo_secuencial = fin_secuencial - inicio_secuencial  # Calcula el tiempo total de ejecucion

# Medir el tiempo de ejecucion en paralelo
inicio_paralelo = time.time()  # Guarda el tiempo de inicio
with concurrent.futures.ThreadPoolExecutor() as executor: 
    # Dividir el rango en subrangos para el paralelismo
    tamanio_rango = 1000  # Tamaño de cada subrango
    subrangos = [range(i, i + tamanio_rango) for i in range(10**6, 10**6 + 10000, tamanio_rango)]  # Divide el rango en subrangos
    
    # Ejecutar la busqueda de primos en paralelo
    resultados_futuros = list(executor.map(encontrar_primos, subrangos))  # Ejecuta encontrar_primos en paralelo
    
    # Unir los resultados
    primos_paralelo = [num for sublist in resultados_futuros for num in sublist]  # Une los resultados de todos los subrangos
fin_paralelo = time.time()  # Guarda el tiempo de finalizacion
tiempo_paralelo = fin_paralelo - inicio_paralelo  # Calcula el tiempo total de ejecucion

# Imprimir los tiempos de ejecución
print(f"Tiempo secuencial: {tiempo_secuencial:.2f} segundos")  # Imprime el tiempo secuencial
print(f"Tiempo paralelo: {tiempo_paralelo:.2f} segundos")  # Imprime el tiempo paralelo
