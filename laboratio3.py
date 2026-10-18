
# ============================================================================
# LABORATORIO TEMA 3: ARREGLOS Y PROCESAMIENTO DE DATOS LINEALES
# ============================================================================


def etapa_1_unidimensional():
    print("\n--- ETAPA 1: EXPLORACIÓN DE LISTAS UNIDIMENSIONALES ---")
    numeros = [12, 45, 7, 23, 89, 34, 56, 90, 3, 67]

    print("Lista inicial de 10 elementos:")
    for i, num in enumerate(numeros):
        print(f"  Índice [{i}]: {num}")

    print("\nModificación del tercer elemento (índice 2):")
    while True:
        try:
            nuevo_valor = int(
                input(
                    f"Ingrese el nuevo valor para el tercer elemento (actual: {numeros[2]}): "
                )
            )
            numeros[2] = nuevo_valor
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    print(f"Lista actualizada: {numeros}")

    print("\nBúsqueda de elemento:")
    try:
        buscar = int(input("Ingrese un número entero para buscar en la lista: "))
        if buscar in numeros:
            posicion = numeros.index(buscar)
            print(
                f"-> El número {buscar} SÍ existe en la lista (encontrado en el índice {posicion})."
            )
        else:
            print(f"-> El número {buscar} NO existe en la lista.")
    except ValueError:
        print("Error: Entrada inválida.")


def etapa_2_bidimensional():
    print("\n--- ETAPA 2: ARREGLOS BIDIMENSIONALES (MATRIZ 3x3) ---")
    matriz = []
    print("Ingrese los valores para llenar la matriz de 3 filas x 3 columnas:")
    for f in range(3):
        fila = []
        for c in range(3):
            while True:
                try:
                    val = int(
                        input(f"  Ingrese valor para Posición [{f}][{c}]: ")
                    )
                    fila.append(val)
                    break
                except ValueError:
                    print("Error: Ingrese un entero válido.")
        matriz.append(fila)

    print("\nMatriz ingresada (Formato Tabular 3x3):")
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:6d}", end="")
        print()

    suma_total = sum(sum(fila) for fila in matriz)
    print(f"\nSuma total de todos los elementos de la matriz: {suma_total}")


def etapa_3_operaciones_listas():
    print("\n--- ETAPA 3: OPERACIONES SOBRE LISTAS DINÁMICAS ---")
    lista_dinamica = [10, 25, 50]

    while True:
        print("\n--- SUBMENÚ OPERACIONES ---")
        print(f"Lista actual: {lista_dinamica}")
        print("1. Insertar un elemento al final")
        print("2. Eliminar un elemento por posición (índice)")
        print("3. Buscar un valor y mostrar su posición")
        print("4. Regresar al menú principal")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            try:
                elem = int(input("Ingrese el número entero a agregar: "))
                lista_dinamica.append(elem)
                print(f"Elemento {elem} insertado al final.")
            except ValueError:
                print("Error: Ingrese un valor entero válido.")

        elif opcion == "2":
            if not lista_dinamica:
                print("La lista está vacía.")
                continue
            try:
                pos = int(
                    input(
                        f"Ingrese el índice a eliminar (0 a {len(lista_dinamica)-1}): "
                    )
                )
                if 0 <= pos < len(lista_dinamica):
                    eliminado = lista_dinamica.pop(pos)
                    print(
                        f"Elemento {eliminado} eliminado de la posición {pos}."
                    )
                else:
                    print("Error: Índice fuera de rango.")
            except ValueError:
                print("Error: Ingrese un índice entero válido.")

        elif opcion == "3":
            try:
                val = int(input("Ingrese el valor que desea buscar: "))
                if val in lista_dinamica:
                    print(
                        f"El valor {val} se encuentra en el índice {lista_dinamica.index(val)}."
                    )
                else:
                    print(f"El valor {val} no está presente en la lista.")
            except ValueError:
                print("Error: Valor inválido.")

        elif opcion == "4":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def etapa_4_ordenamiento():
    print("\n--- ETAPA 4: ALGORITMOS DE ORDENAMIENTO ---")
    datos_originales = [64, 34, 25, 12, 22, 11, 90]
    print(f"Lista desordenada inicial: {datos_originales}")

    # --- Ordenamiento Burbuja ---
    burbuja = datos_originales.copy()
    n = len(burbuja)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if burbuja[j] > burbuja[j + 1]:
                burbuja[j], burbuja[j + 1] = burbuja[j + 1], burbuja[j]

    print("\n[Burbuja] Lista antes :", datos_originales)
    print("[Burbuja] Lista después:", burbuja)

    # --- Ordenamiento Selección ---
    seleccion = datos_originales.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if seleccion[j] < seleccion[min_idx]:
                min_idx = j
        seleccion[i], seleccion[min_idx] = seleccion[min_idx], seleccion[i]

    print("\n[Selección] Lista antes :", datos_originales)
    print("[Selección] Lista después:", seleccion)


def main():
    while True:
        print("\n==================================================")
        print(" LABORATORIO TEMA 3: LISTAS Y ARREGLOS EN PYTHON ")
        print("==================================================")
        print("1. Ejecutar Etapa 1: Arreglos Unidimensionales")
        print("2. Ejecutar Etapa 2: Arreglos Bidimensionales (Matriz 3x3)")
        print("3. Ejecutar Etapa 3: Operaciones sobre Listas (Menú)")
        print("4. Ejecutar Etapa 4: Algoritmos de Ordenamiento")
        print("5. Salir del Programa")

        opc = input("Seleccione una opción (1-5): ").strip()

        if opc == "1":
            etapa_1_unidimensional()
        elif opc == "2":
            etapa_2_bidimensional()
        elif opc == "3":
            etapa_3_operaciones_listas()
        elif opc == "4":
            etapa_4_ordenamiento()
        elif opc == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Seleccione un número entre 1 y 5.")


if __name__ == "__main__":
    main()
