#Libreria numpy
import numpy as np

#Defino la funcion a trabajar Q(t) (la funcion que me presentan en el ejercicio)
def Q(t):
    return 2 + t**2 #2+t^2

#Defino mi intervalo (tambien dado en el ejercicio) 
a = 0.0
b = 4.0
valor_exacto = 88.0 / 3.0  #resultado de la integral exacta de Q(t) en el intervalo [0, 4]

subintervalos = [2, 4, 8] #subintervalos dados con los cuales trabajar 

print(f"\n{'n':<5} | {'Aprox (Litros)':<15} | {'Error Absoluto':<15}")
print("---------------------------------------------------")

#for para cada cantidad de subintervalos, donde calculo la integral aproximada y el error absoluto
for n in subintervalos:
    h = (b - a) / n #formula para sacar h
    t = np.linspace(a, b, n + 1)  #a es mi intervalo inferior, b es mi intervalo superior y n+1 es la cantidad de puntos que se necesitan para dividir el intervalo en n subintervalos.
    #np.linspace() es una funcion que genera un arreglo de numeros equispaciados entre a y b.
    y = Q(t)
    
    # Regla del Trapecio compuesta
    #utilizo la regla del trapecio compuesta en lugar de la simple por que la compuesta divide todo el intervalo de integracion [a,b]
    #en varios subintervalos mas pequenios de ancho de h y aplica la regla del trapecio en cada uno de estos.
    
    #Suma de extremos + 2 * suma de puntos interiores
    integral_trapecio = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1]) #np.sum() es una funcion que sirve como sumatoria.
    #al final de la formula se utiliza y[-1] para sumar el ultimo valor de mi funcion, seria como f(tn), donde ambos representan el extremo final de mi intervalo de integracion [a,b]
    
    #calculo del error absoluto entre el valor exacto y el aproximado
    error_abs = abs(valor_exacto - integral_trapecio)
    
    print(f"{n:<5} | {integral_trapecio:<15.4f} | {error_abs:<15.4f}")



print("---------------------------------------------------\n")
print(f"Valor exacto de la integral con el intervalo de [0,4] = {valor_exacto:.4f} litros\n")