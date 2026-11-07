#libreria numpy
import numpy as np

#funcion del ejercicio
def v(t):
    return 1 + t**2

#intervalos dados en el ejercicio
a = 0.0
b = 3.0
valor_exacto = 12.0 # valor exacto resultante de la integral definida

#subintervalos dados en el ejercicio 
subintervalos = [3, 6, 9]

print(f"{'n':<5} | {'Aprox':<12} | {'Error Absoluto':<15}")
print("-----------------------------------------------------")

for n in subintervalos:
    #Para poder utilizar la regla de Simpson 3/8 hay que validar que n sea múltiplo de 3
    if n % 3 != 0:
        print(f"Error: n={n} no es múltiplo de 3. Simpson 3/8 requiere n múltiplo de 3.")
        continue
    #formula de h  
    h = (b - a) / n
    t = np.linspace(a, b, n + 1)
    y = v(t)
    
    # Regla de Simpson 3/8 compuesta
    # Coeficientes: extremos 1, múltiplos de 3 internos 2, y los demás 3. 
    #sigue el patron de 1, 3, 3, 2.
    suma_multiplos_3 = np.sum(y[3:-3:3]) if n >= 6 else 0
    
    #creo una lista con los numeros que no son multiplos de 3, para poder sumarlos y multiplicarlos por 3 en la formula de la regla de simpson 3/8 compuesta
    no_multiplos_3 = [i for i in range(1, n) if i % 3 != 0]
    suma_otros = np.sum(y[no_multiplos_3]) #los que no son multiplos de 3 los sumo y luego los multiplico por 3 en la formula de la regla de simpson 3/8 compuesta
    
    #formula de la regla de simpson 3/8 compuesta
    integral_simpson38 = ((3 * h) / 8) * (y[0] + 3 * suma_otros + 2 * suma_multiplos_3 + y[-1])
    error_abs = abs(valor_exacto - integral_simpson38)
    
    print(f"{n:<5} | {integral_simpson38:<12.4f} | {error_abs:<15.4f}")

print("-----------------------------------------------------")
print(f"Valor exacto de referencia: {valor_exacto:.4f}")