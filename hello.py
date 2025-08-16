opciones = ("soleado", "nublado", "lluvia", "nieve")

print("Seleccione el clima:")
for i, opcion in enumerate(opciones, 1):
    print(f"{i}. {opcion}")

while True:
    try:
        seleccion = int(input("Ingrese el número de opción: ")) - 1
        if 0 <= seleccion < len(opciones):
            clima = opciones[seleccion]
            print(f"Ha seleccionado: {clima}")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    except ValueError:
        print("Por favor ingrese un número válido.")

# emitir por consola un dibujo de la manzana mordida de apple con ASCII
print("")


