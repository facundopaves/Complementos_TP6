#importo la libreria numpy
import numpy as np

#Defino la funcion del ejercicio
def f(x):
    return np.exp(-x**2) #e^(-x^2)
 
#intervalo dado
a = 0.0
b = 1.0

val_referencia = 0.7468241328  # Valor de alta precisión

#Defino las funciones para cada método

#regla del trapecio  
def regla_del_trapecio(a, b, n):
    h = (b - a) / n
    t = np.linspace(a, b, n + 1)
    y = f(t)
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

#Regla de Simpson 1/3
def regla_simpson_1_3(a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson 1/3 requiere n par.")
    h = (b - a) / n
    t = np.linspace(a, b, n + 1)
    y = f(t)
    suma_impares = np.sum(y[1:-1:2])
    suma_pares = np.sum(y[2:-2:2]) if n > 2 else 0
    return (h / 3) * (y[0] + 4 * suma_impares + 2 * suma_pares + y[-1])

#Regla de simpson 3/8
def regla_simpson_3_8(a, b, n):
    if n % 3 != 0:
        raise ValueError("Simpson 3/8 requiere n múltiplo de 3.")
    h = (b - a) / n
    t = np.linspace(a, b, n + 1)
    y = f(t)
    suma_multiplos_3 = np.sum(y[3:-3:3]) if n >= 6 else 0
    indices_otros = [i for i in range(1, n) if i % 3 != 0]
    suma_otros = np.sum(y[indices_otros])
    return ((3 * h) / 8) * (y[0] + 3 * suma_otros + 2 * suma_multiplos_3 + y[-1])


#Comparacion para los n solicitados en la consigna
print("--- MÉTODO DEL TRAPECIO (n = 4, 8, 16, 32) ---")
n_trapecio = [4, 8, 16, 32]
for n in n_trapecio:
    aprox = regla_del_trapecio(a, b, n)
    error = abs(val_referencia - aprox)
    print(f"n = {n:<2} | Aprox: {aprox:.8f} | Error Abs: {error:.8e}")

print("\n--- MÉTODO DE SIMPSON 1/3 (n = 4, 8, 16, 32) ---")
n_simp13 = [4, 8, 16, 32]
for n in n_simp13:
    aprox = regla_simpson_1_3(a, b, n)
    error = abs(val_referencia - aprox)
    print(f"n = {n:<2} | Aprox: {aprox:.8f} | Error Abs: {error:.8e}")

print("\n--- MÉTODO DE SIMPSON 3/8 (n = 3, 6, 12, 24) ---")
n_simp38 = [3, 6, 12, 24]
for n in n_simp38:
    aprox = regla_simpson_3_8(a, b, n)
    error = abs(val_referencia - aprox)
    print(f"n = {n:<2} | Aprox: {aprox:.8f} | Error Abs: {error:.8e}")
    


#Convergencia: 
#A medida que incrementamos la cantidad de subintervalos (n), los tres métodos convergen de forma muy rápida hacia el valor de referencia de alta precisión. 
# Esto indica que todos los métodos son efectivos para poder aproximarme a la funcion que me dieron.


#Orden de aproximación:La Regla del Trapecio reduce su error de truncamiento a un cuarto (O(h^2)) cada vez que duplicamos n.
#Las Reglas de Simpson (1/3 y 3/8) muestran una convergencia mucho más acelerada (O(h^4))
#alcanzando precisiones de varios decimales exactos con valores de n considerablemente más bajos.

#Pregunta de análisis

#¿Qué método logra mayor precisión para un costo computacional comparable?
#Las reglas de Simpson (1/3 y 3/8) logran una precisión muy superior a la del Trapecio para un costo computacional prácticamente idéntico (medido en cantidad de evaluaciones de la función)
#ya que su error decae con la cuarta potencia del paso (h^4) en comparación con el orden cuadrático (h^2) del trapecio.


#¿Qué limitaciones tiene esa conclusión?
#La principal limitación es que las reglas de Simpson exigen restricciones estrictas sobre la cantidad de subintervalos (n debe ser par para Simpson 1/3 y múltiplo de 3 para Simpson 3/8)
#mientras que la regla del Trapecio puede aplicarse con cualquier valor entero de n (debido a que no tiene restricciones)
#dando asi menor limitacion en problemas de muestreo experimental donde la cantidad de puntos es fija o irregular.