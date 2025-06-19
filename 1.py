## Problema 1: Control de Temperatura en un Invernadero (25 pts)

# **Enunciado:**  
# Un agricultor necesita monitorear la temperatura de su invernadero para asegurar el crecimiento óptimo de sus plantas.
#  Debes ayudarle a identificar si las temperaturas registradas están dentro del rango adecuado y alertar si alguna es peligrosa.

# **Indicaciones paso a paso:**
# 1. Solicita al usuario que ingrese 5 temperaturas.
# 2. Guarda las temperaturas en una lista.
# 3. Calcula el promedio y la temperatura máxima.
# 4. Verifica si todas las temperaturas están entre 15°C y 30°C.
# 5. Si alguna temperatura está fuera de 10°C–35°C, muestra una advertencia.

# **Puntos asignados:** 25 pts

# **Criterios evaluados:**
# - Uso correcto de lista y cálculos (10 pts)
# - Evaluación de condiciones lógicas (10 pts)
# - Orden y claridad del código (5 pts)

temperaturas = []
for i in range(5):
    temp = int(input("Ingresa una temperatura: "))
    temperaturas.append(temp)

promedio_temperaturas = sum(temperaturas)/len(temperaturas)
t_max = max(temperaturas)

check = True
for t in temperaturas:
    if t < 15 or >30:
        check = False
        break

if check:
    print()