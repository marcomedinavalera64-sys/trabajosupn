
# ============================================================================
# LABORATORIO TEMA 4: CADENAS DE CARACTERES Y ARREGLOS PARALELOS
# ============================================================================

def etapa_1_manipulacion_cadenas():
    print("\n--- ETAPA 1: METODOS COMUNES DE MANIPULACION DE CADENAS ---")
    texto_original = "   Fundamentos de Programacion en Python y C# - UPN 2026   "
    print(f"Texto original: '{texto_original}'")

    # Limpieza de espacios en extremos
    texto_limpio = texto_original.strip()
    print(f"1. Texto limpio (.strip()): '{texto_limpio}'")

    # Subcadena (slicing)
    subcadena = texto_limpio[0:11]
    print(f"2. Subcadena [0:11]: '{subcadena}'")

    # Busqueda de posicion (find / index)
    posicion = texto_limpio.find("Programacion")
    print(f"3. Posicion de 'Programacion' (.find()): {posicion}")

    # Reemplazo de subcadena (replace)
    texto_reemplazado = texto_limpio.replace("Python y C#", "Lenguajes Modernos")
    print(f"4. Texto reemplazado (.replace()): '{texto_reemplazado}'")

    # Separacion en lista (split)
    lista_palabras = texto_limpio.split(" ")
    print(f"5. Texto separado en lista (.split()): {lista_palabras}")


def etapa_2_arreglos_paralelos():
    print("\n--- ETAPA 2: BUSQUEDA EN ARREGLOS PARALELOS ---")
    estudiantes = ["Efren", "Cristian", "Anderson", "Marco", "Walter"]
    edades = [19, 20, 18, 21, 19]

    print("Listado de estudiantes y edades (Arreglos Paralelos):")
    for i in range(len(estudiantes)):
        print(f"  Index [{i}] -> Estudiante: {estudiantes[i]} | Edad: {edades[i]}")

    nombre_buscar = input("\nIngrese el nombre del estudiante a buscar: ").strip()
    encontrado = False

    for i in range(len(estudiantes)):
        if estudiantes[i].lower() == nombre_buscar.lower():
            print(f"-> Resultado: {estudiantes[i]} tiene {edades[i]} años (Encontrado en indice [{i}]).")
            encontrado = True
            break

    if not encontrado:
        print(f"-> Resultado: El estudiante '{nombre_buscar}' no se encuentra en el registro.")


def etapa_3_estructuras_combinadas():
    print("\n--- ETAPA 3: BUSQUEDA TEXTUAL EN ESTRUCTURAS COMBINADAS ---")

    # Lista de diccionarios que representan registros de usuarios
    usuarios = [
        {"nombre": "Efren Araujo", "email": "efren@upn.pe", "ciudad": "Cajamarca"},
        {"nombre": "Cristian Burga", "email": "cristian@upn.pe", "ciudad": "Lima"},
        {"nombre": "Anderson Cabanillas", "email": "anderson@upn.pe", "ciudad": "Cajamarca"},
        {"nombre": "Marco Medina", "email": "marco@upn.pe", "ciudad": "Trujillo"},
        {"nombre": "Walter Mestanza", "email": "walter@upn.pe", "ciudad": "Cajamarca"}
    ]

    print("Registros de usuarios cargados:")
    for usr in usuarios:
        print(f" - {usr['nombre']} | {usr['email']} | Ciudad: {usr['ciudad']}")

    ciudad_buscar = input("\nIngrese la ciudad para filtrar usuarios: ").strip()
    print(f"\nCoincidencias encontradas para la ciudad '{ciudad_buscar}':")
    coincidencias = 0

    for usr in usuarios:
        if usr["ciudad"].lower() == ciudad_buscar.lower():
            print(f" -> Nombre: {usr['nombre']} | Email: {usr['email']}")
            coincidencias += 1

    if coincidencias == 0:
        print(" -> No se encontraron usuarios registrados en esa ciudad.")


def etapa_4_ordenamiento_cadenas():
    print("\n--- ETAPA 4: ORDENAMIENTO ALFABETICO DE CADENAS ---")
    nombres = ["Mestanza Walter", "Araujo Efren", "Cabanillas Anderson", "Burga Cristian", "Medina Marco"]
    print(f"Lista de nombres desordenada: {nombres}")

    # Algoritmo de ordenamiento por Seleccion para cadenas
    n = len(nombres)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nombres[j].lower() < nombres[min_idx].lower():
                min_idx = j
        nombres[i], nombres[min_idx] = nombres[min_idx], nombres[i]

    print(f"Lista de nombres ordenada alfabeticamente (Seleccion): {nombres}")


def main():
    while True:
        print("\n============================================================")
        print(" LABORATORIO TEMA 4: CADENAS Y ARREGLOS PARALELOS EN PYTHON")
        print("============================================================")
        print("1. Ejecutar Etapa 1: Manipulacion de Cadenas (Metodos)")
        print("2. Ejecutar Etapa 2: Arreglos Paralelos (Nombres y Edades)")
        print("3. Ejecutar Etapa 3: Estructuras Combinadas (Busqueda por Ciudad)")
        print("4. Ejecutar Etapa 4: Ordenamiento Alfabetico de Cadenas")
        print("5. Salir del Programa")

        opc = input("Seleccione una opción (1-5): ").strip()

        if opc == "1":
            etapa_1_manipulacion_cadenas()
        elif opc == "2":
            etapa_2_arreglos_paralelos()
        elif opc == "3":
            etapa_3_estructuras_combinadas()
        elif opc == "4":
            etapa_4_ordenamiento_cadenas()
        elif opc == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Seleccione un número entre 1 y 5.")


if __name__ == "__main__":
    main()
