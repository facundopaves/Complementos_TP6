#libreria numpy
import numpy as np



#Funcion dada en el ejercicio
def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5 #0.2 + 25x - 200x^2 + 675x^3 - 900x^4 + 400x^5

print("\n--- METODOS DE INTEGRACION NUMERICA ---\n")

print("funcion: f(x) = 0.2 + 25x - 200x^2 + 675x^3 - 900x^4 + 400x^5")

#intervalos dados en el ejercicio
a = 0.0
b = 0.8

# Integral exacta = 1.0688 
val_exacto = 1.0688

print("\n-------------------------------------------------------------------------------")
print(f"{'Metodo':<30} | {'n':<4} | {'Aprox':<10} | {'Error Absoluto':<15}")
print("-------------------------------------------------------------------------------")

#metodo del trapecio simple (n=1)
h = b - a
ap_a = (h / 2) * (f(a) + f(b))
print(f"{'a) Trapecio simple':<30} | {1:<4} | {ap_a:<10.4f} | {abs(val_exacto - ap_a):<15.4f}")

#metodo del trapecio n=2
n = 2
h = (b - a) / n
x = np.linspace(a, b, n + 1)
y = f(x)
ap_b = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
print(f"{'b) Trapecio':<30} | {n:<4} | {ap_b:<10.4f} | {abs(val_exacto - ap_b):<15.4f}")

#metodo de Simpson 1/3 (n=2)
ap_c = (h / 3) * (y[0] + 4 * y[1] + y[2])
print(f"{'c) Simpson 1/3':<30} | {n:<4} | {ap_c:<10.4f} | {abs(val_exacto - ap_c):<15.4f}")

#metodo de Simpson 1/3 múltiple (n=4)
n = 4
h = (b - a) / n
x = np.linspace(a, b, n + 1)
y = f(x)
ap_d = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
print(f"{'d) Simpson 1/3 múltiple':<30} | {n:<4} | {ap_d:<10.4f} | {abs(val_exacto - ap_d):<15.4f}")

#metodo de Simpson 3/8 (n=3)
n = 3
h = (b - a) / n
x = np.linspace(a, b, n + 1)
y = f(x)
ap_e = ((3 * h) / 8) * (y[0] + 3 * y[1] + 3 * y[2] + y[3])
print(f"{'e) Simpson 3/8':<30} | {n:<4} | {ap_e:<10.4f} | {abs(val_exacto - ap_e):<15.4f}")

print("-------------------------------------------------------------------------------")


#Conclusiones:

#¿Que sucede al aumentar el subintervalo n?:
#al aumentar n, cualquiera de los metodos reduce drasticamente el error absoluto, es decir, la aproximacion se acerca mucho mas al valor exacto de la integral

#Comparacion entre metodos:
#el metodo de Simpson 1/3 múltiple es el que tiene menor error absoluto, es decir que es el metodo que mejor se aproxima al valor exacto de la integral

#Variaciones de los metodos:
#El trapecio es el cual tiene mayor error absoluto pero a la vez mayor flexibilidad para admitir cualquier valor de n
#Simpson 1/3 exige que n sea par y Simpson 3/8 exige que n sea multiplo de 3, lo cual limita la cantidad de subintervalos que se pueden utilizar para aproximar la integral
