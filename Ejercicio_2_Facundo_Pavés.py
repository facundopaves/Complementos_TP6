#Libreria numpy
import numpy as np

#Defino la funcion dada en el ejercicio 
def P(t):
    return 1 + t**3 #la funcion es 1+t^3

#Defino el intervalo dado en mi ejercicio
a = 0.0
b = 2.0
#el valor exacto de la integral exacta
valor_exacto = 6.0

#subintervalos dados en el ejercicio con los cuales voy a operar
subintervalos = [2, 4, 8]


print(f"{'n':<5} | {'Aprox':<12} | {'Error Absoluto':<15}")
print("------------------------------------------")

#for n para la cantidad de subintervalos, donde calculo la integral aproximada y el error abosluto
for n in subintervalos:
    #Lo primero que debo hacer para utilizar la regla de simpson 1/3 es verificar que n sea par, ya que si es impar no puedo utilizar la regla
    if n % 2 != 0:
        print(f"Error: n={n} es impar. Simpson 1/3 requiere n par.")
        continue
    
    # formula para el calculo de h
    h = (b - a) / n
    
    t = np.linspace(a, b, n + 1)
    y = P(t)
    
    # Regla de Simpson 1/3 compuesta
    # Extremos (y[0] y y[-1]) con coef 1
    # Puntos impares con coef 4, puntos pares internos con coef 2
    suma_impares = np.sum(y[1:-1:2])
    suma_pares = np.sum(y[2:-2:2]) if n > 2 else 0
    
    #formula de la regla de simpson 1/3 compuesta
    integral_simpson = (h / 3) * (y[0] + 4 * suma_impares + 2 * suma_pares + y[-1])
    
    #calculo del error absoluto entre el valor exacto y el aproximado de la regla de simpson 1/3 compuesta
    error_abs = abs(valor_exacto - integral_simpson)
    
    print(f"{n:<5} | {integral_simpson:<12.4f} | {error_abs:<15.4f}")

print("------------------------------------------")
print(f"Valor exacto de la integral con el intervalo de [0,2] : {valor_exacto:.4f}")