# SISTEMA DE REGISTRO DE NOTAS DEL SALÓN

# Inicializar listas paralelas
nombres = []
notas = []

print("=== Registro de Notas del Grupo ===")

# Solicitar cantidad de estudiantes
cantidad = int(input("¿Cuántos estudiantes hay en el grupo? "))

# Registrar nombre y nota de cada estudiante
for i in range(cantidad):
    nombre = input(f"Nombre del estudiante {i+1}: ")
    while True:
        try:
            nota = float(input(f"Nota de {nombre} (0 a 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("Error: la nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: ingrese un número válido.")
    
    nombres.append(nombre)
    notas.append(nota)

# Mostrar reporte individual
print("\n=== REPORTE DE ESTUDIANTES ===")
for i in range(cantidad):
    estado = "Aprobó" if notas[i] >= 3.0 else "Reprobó"
    print(f"{nombres[i]} - Nota: {notas[i]} - {estado}")

# Calcular estadísticas
promedio = sum(notas) / len(notas)
nota_max = max(notas)
nota_min = min(notas)
aprobados = sum(1 for n in notas if n >= 3.0)
reprobados = len(notas) - aprobados

# Mostrar resultados generales
print("\n=== RESULTADOS GENERALES ===")
print(f"Promedio del grupo: {promedio:.2f}")
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")

# Evaluar desempeño general del grupo
if promedio >= 3.5:
    print("El grupo APROBÓ en general.")
else:
    print("El grupo NECESITA REFUERZO.")

# Reto Bonus: búsqueda por nombre
print("\n=== BÚSQUEDA DE ESTUDIANTE ===")
buscar = input("Ingrese el nombre del estudiante a buscar: ")
if buscar in nombres:
    indice = nombres.index(buscar)
    print(f"{buscar} tiene una nota de {notas[indice]}")
else:
    print("Estudiante no encontrado.")
