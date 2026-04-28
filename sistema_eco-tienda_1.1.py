# ______________________________________________________________
# SISTEMA "ECO-TIENDA" - Gestión dinámica de  ventas
# Autor: Yordy 
# Descripción:
#   Este sistema simula una caja registradora de un supermercado.
#   Permite ingresar múltiples productos con nombre y precio,
#   valida errores de entrada, calcula descuentos y genera
#   una factura detallada al finalizar la compra.
# _______________________________________________________________

# Listas vacías para almacenar productos y precios
lista_nombre_producto = []
lista_precios = []

#Mensaje de bienvenida, es meramente estetico
print('-' * 50)
print("=== Bienvenido al sistema ECO-TIENDA ===")
print("Ingrese los productos uno por uno. Escriba 'PAGAR' para finalizar la compra.\n")
print('-' * 50)
    

# Bucle infinito para registrar productos hasta que se escriba 'PAGAR'
while True:
    print('¨' * 50)
    try:
        # Solicitar nombre del producto
        nombre = input("Ingrese el nombre del producto o 'PAGAR' para terminar: ").strip()

        # Condición de salida
        if nombre.upper() == "PAGAR":
            break

        # Solicitar precio del producto
        while True:
            try:
                precio = float(input(f"Ingrese el precio de '{nombre}': ").strip())

                # Validación: precio no puede ser negativo
                if precio < 0:
                    print("Error: Dato invalido. Por favor volver a ingresar precio.")
                    continue

                # Si pasa la validaciones, se guarda en las listas
                lista_nombre_producto.append(nombre)
                lista_precios.append(precio)
                break
            except ValueError:
                print("Error: Dato inválido. Por favor vuelva a ingresar el precio en números.")

    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Error inesperado: {e}. El sistema seguirá funcionando.\n")
print('¨' * 50)


# ============================================================
# FACTURA DETALLADA
# ============================================================
print('_' * 50)
print("\n=== FACTURA DETALLADA ===")

# Recorrer listas y mostrar productos con precios
for i in range(len(lista_nombre_producto)):
    print(f"{lista_nombre_producto[i]}..........${lista_precios[i]:,.0f}")

# Calcular total
total = 0
for precio in lista_precios:
    total += precio

print(f"\nPrecio total de los productos: ${total:,.0f}")

# Aplicar descuentos según condiciones
descuento = 0
cantidad_productos = len(lista_precios)

if total >= 150000 and cantidad_productos >= 5:
    descuento = 0.15  # 15%
    print("Descuento aplicado: 15%")
elif total >= 100000 and total < 149000 and cantidad_productos <= 5:
    descuento = 0.05  # 5%
    print("Descuento aplicado: 5%")
else:
    print("Sin Descuento")

# Calcular total con descuento si aplica
if descuento > 0:
    total_con_descuento = total - (total * descuento)
    print(f"Total a pagar con descuento: ${total_con_descuento:,.0f}")
else:
    print(f"Total a pagar: ${total:,.0f}")

print("\n=== Gracias por su compra en ECO-TIENDA ===")
print('_' * 50)
