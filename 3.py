## Problema 3: Sistema de Acceso Condicional (20 pts)

# **Enunciado:**  
# En una empresa, el acceso a una zona restringida depende de la edad, el rol de supervisor y la autorización especial. Debes crear un sistema que determine si una persona puede ingresar.

# **Indicaciones paso a paso:**
# 1. Solicita al usuario su edad, si es supervisor y si tiene autorización.
# 2. Verifica si puede acceder: debe ser mayor de edad y cumplir al menos una condición (ser supervisor o tener autorización).
# 3. Muestra un mensaje indicando si el acceso está permitido o denegado.

# **Puntos asignados:** 20 pts

# **Criterios evaluados:**
# - Uso correcto de operadores lógicos (10 pts)
# - Validación de condiciones y entrada de datos (5 pts)
# - Claridad de la salida (5 pts)

edad = int(input("¿Cuantos años tienes? "))
sup = input("¿Eres supervisor? (s/n) ").lower()
autoriza = input("¿Tienes autorización? (s/n) ").lower()

es_mayor_edad = (edad >= 18)
cumple_condiciones = (sup or autoriza)
acceso_permitido = (cumple_condiciones and edad)

if acceso_permitido:
    print("Puedes Acceder")
else:
    print("Andate de acá bobolón")