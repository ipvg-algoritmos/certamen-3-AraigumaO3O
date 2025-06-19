## Problema 2: Análisis de Notas de Evaluación (35 pts)

# **Enunciado:**  
# En una clase, se registran las notas de 3 estudiantes en 3 asignaturas. El profesor necesita saber los promedios y si todos aprobaron, 
# además de alertar si algún estudiante tiene bajo rendimiento.

# **Indicaciones paso a paso:**
# 1. Crea una matriz 3x3 para guardar las notas.
# 2. Calcula el promedio de cada estudiante (por fila) y de cada asignatura (por columna).
# 3. Verifica si todos los estudiantes aprobaron (nota >= 4.0).
# 4. Muestra una alerta si algún promedio individual es menor a 3.5.

# **Puntos asignados:** 35 pts

# **Criterios evaluados:**
# - Representación correcta de la matriz (10 pts)
# - Cálculo de promedios por fila y columna (10 pts)
# - Evaluación lógica de condiciones (10 pts)
# - Claridad en mensajes y formato (5 pts)

notas = [[7.0, 2.2, 2.6],
         [6.0, 4.6, 5.8],
         [6.7, 2.6, 3.5]]
for fila in range(3):
    suma = 0
    for col in range(3):
        suma += notas[fila][col]
    