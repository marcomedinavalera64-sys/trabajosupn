import hashlib
from functools import reduce

# ==========================================
# 1. EXCEPCIONES Y MODELO DE OBJETOS (POO)
# ==========================================

class ValidacionError(Exception):
    pass


class Usuario:
    """Usuario del sistema con contraseña encriptada (SHA-256)."""

    def __init__(self, id_u: str, nombre: str, clave: str):
        self.id_u = id_u
        self.nombre = nombre
        self.__hash = hashlib.sha256(clave.encode()).hexdigest()

    def autenticar(self, clave_ingresada: str) -> bool:
        return self.__hash == hashlib.sha256(
            clave_ingresada.encode()
        ).hexdigest()


class Paciente:
    """Paciente con enmascaramiento de DNI (Ley N.° 29733)."""

    def __init__(self, id_p: str, nombre: str, dni: str, edad: int):
        self.id_p = id_p
        self.nombre = nombre
        self.dni = dni  # Usa el setter con validación
        self.edad = edad

    @property
    def dni_protegido(self) -> str:
        """Muestra solo los últimos 3 dígitos para proteger la privacidad."""
        return f"*****{self.__dni[-3:]}"

    @property
    def dni_real(self) -> str:
        return self.__dni

    @property
    def dni(self) -> str:
        return self.__dni

    @dni.setter
    def dni(self, valor: str):
        if not valor.isdigit() or len(valor) != 8:
            raise ValidacionError(
                "El DNI debe tener exactamente 8 dígitos numéricos."
            )

        self.__dni = valor


class Cita:
    """Cita médica con control de estados."""

    ESTADOS = ["PROGRAMADA", "ATENDIDA", "CANCELADA"]

    def __init__(self, id_c: str, paciente: Paciente, fecha: str):
        self.id_c = id_c
        self.paciente = paciente
        self.fecha = fecha
        self.__estado = "PROGRAMADA"

    @property
    def estado(self) -> str:
        return self.__estado

    @estado.setter
    def estado(self, valor: str):
        if valor.upper() not in self.ESTADOS:
            raise ValidacionError(
                f"Estado no válido. Use: {self.ESTADOS}"
            )

        self.__estado = valor.upper()


# ==========================================
# 2. PARADIGMA FUNCIONAL (PROCESAMIENTO)
# ==========================================

class FuncionalReportes:

    @staticmethod
    def filtrar_programadas(citas: list[Cita]) -> list[Cita]:
        """filter(): Filtra citas en estado PROGRAMADA."""
        return list(
            filter(lambda c: c.estado == "PROGRAMADA", citas)
        )

    @staticmethod
    def mapear_resumen(pacientes: list[Paciente]) -> list[dict]:
        """map(): Transforma la lista a un resumen seguro con DNI protegido."""

        return list(
            map(
                lambda p: {
                    "ID": p.id_p,
                    "Nombre": p.nombre,
                    "DNI_Protegido": p.dni_protegido,
                    "Edad": p.edad
                },
                pacientes
            )
        )

    @staticmethod
    def promedio_edad(pacientes: list[Paciente]) -> float:
        """reduce(): Calcula la edad promedio acumulada."""

        if not pacientes:
            return 0.0

        return reduce(
            lambda acc, p: acc + p.edad,
            pacientes,
            0
        ) / len(pacientes)


# ==========================================
# 3. INTERFAZ INTERACTIVA (SISTEMA INTERACTIVO)
# ==========================================

def iniciar_sistema():

    print("======================================================")
    print(" CENTRO DE SALUD RURAL 'SANTA ROSA' - CHUGUR")
    print(" MÓDULO INTERACTIVO DE GESTIÓN OPERATIVA")
    print("======================================================")

    # Base de datos local en memoria
    pacientes_db: list[Paciente] = []
    citas_db: list[Cita] = []

    # Crear usuario administrador por defecto
    admin = Usuario(
        "U01",
        "Recepcionista Santa Rosa",
        "Chugur2026"
    )

    # Sistema de Autenticación
    print("\n--- INICIO DE SESIÓN EN EL SISTEMA ---")

    intentos = 0
    autenticado = False

    while intentos < 3 and not autenticado:

        clave = input(
            "Ingrese la contraseña de acceso "
            "(Predeterminada: Chugur2026): "
        )

        if admin.autenticar(clave):
            autenticado = True
            print("✓ Acceso concedido exitosamente.\n")

        else:
            intentos += 1

            print(
                f"❌ Contraseña incorrecta. "
                f"Intentos restantes: {3 - intentos}\n"
            )

    if not autenticado:
        print(
            "Demasiados intentos fallidos. "
            "Cerrando el sistema..."
        )
        return

    # Menú Principal
    while True:

        print("\n" + "=" * 40)
        print(" MENÚ PRINCIPAL")
        print("=" * 40)

        print("1. Registrar nuevo paciente")
        print("2. Registrar nueva cita médica")
        print("3. Cambiar estado de una cita")
        print("4. Ver citas pendientes (filter)")
        print("5. Ver listado protegido de pacientes (map)")
        print("6. Ver edad promedio de pacientes (reduce)")
        print("7. Salir del sistema")

        opcion = input(
            "\nSeleccione una opción (1-7): "
        ).strip()

        try:

            # ==========================================
            # OPCIÓN 1 - REGISTRAR PACIENTE
            # ==========================================

            if opcion == "1":

                print("\n--- REGISTRO DE PACIENTE ---")

                id_p = f"P{len(pacientes_db) + 1:02d}"

                nombre = input(
                    "Ingrese nombre y apellido del paciente: "
                ).strip()

                dni = input(
                    "Ingrese DNI (8 dígitos): "
                ).strip()

                edad = int(
                    input("Ingrese edad del paciente: ")
                )

                if edad <= 0 or edad > 120:
                    raise ValidacionError(
                        "La edad ingresada no es válida."
                    )

                nuevo_paciente = Paciente(
                    id_p,
                    nombre,
                    dni,
                    edad
                )

                pacientes_db.append(nuevo_paciente)

                print(
                    f"✓ Paciente '{nombre}' registrado con éxito. "
                    f"[ID: {id_p}]"
                )


            # ==========================================
            # OPCIÓN 2 - REGISTRAR CITA
            # ==========================================

            elif opcion == "2":

                print("\n--- REGISTRO DE CITA MÉDICA ---")

                if not pacientes_db:
                    print(
                        "⚠️ Debe registrar al menos un paciente "
                        "antes de programar una cita."
                    )
                    continue

                print("Lista de pacientes registrados:")

                for p in pacientes_db:
                    print(
                        f" [{p.id_p}] {p.nombre} "
                        f"- DNI: {p.dni_protegido}"
                    )

                id_p_sel = input(
                    "Ingrese el ID del paciente para la cita: "
                ).strip().upper()

                paciente_encontrado = next(
                    (
                        p
                        for p in pacientes_db
                        if p.id_p == id_p_sel
                    ),
                    None
                )

                if not paciente_encontrado:
                    print(
                        "❌ No se encontró ningún paciente "
                        "con ese ID."
                    )
                    continue

                id_c = f"C{len(citas_db) + 1:02d}"

                fecha = input(
                    "Ingrese fecha y hora de la cita "
                    "(ej. 2026-09-10 09:00): "
                ).strip()

                nueva_cita = Cita(
                    id_c,
                    paciente_encontrado,
                    fecha
                )

                citas_db.append(nueva_cita)

                print(
                    f"✓ Cita registrada para "
                    f"{paciente_encontrado.nombre} "
                    f"el {fecha}. [ID: {id_c}]"
                )


            # ==========================================
            # OPCIÓN 3 - CAMBIAR ESTADO DE CITA
            # ==========================================

            elif opcion == "3":

                print("\n--- CAMBIO DE ESTADO DE CITA ---")

                if not citas_db:
                    print(
                        "⚠️ No hay citas registradas "
                        "en el sistema."
                    )
                    continue

                for c in citas_db:
                    print(
                        f" [{c.id_c}] "
                        f"Paciente: {c.paciente.nombre} | "
                        f"Fecha: {c.fecha} | "
                        f"Estado actual: {c.estado}"
                    )

                id_c_sel = input(
                    "Ingrese el ID de la cita a modificar: "
                ).strip().upper()

                cita_encontrada = next(
                    (
                        c
                        for c in citas_db
                        if c.id_c == id_c_sel
                    ),
                    None
                )

                if not cita_encontrada:
                    print("❌ Cita no encontrada.")
                    continue

                nuevo_estado = input(
                    "Ingrese nuevo estado "
                    "(PROGRAMADA / ATENDIDA / CANCELADA): "
                ).strip()

                cita_encontrada.estado = nuevo_estado

                print(
                    f"✓ Estado de la cita {id_c_sel} "
                    f"actualizado a "
                    f"'{cita_encontrada.estado}'."
                )


            # ==========================================
            # OPCIÓN 4 - VER CITAS PENDIENTES
            # ==========================================

            elif opcion == "4":

                print(
                    "\n--- CITAS PENDIENTES "
                    "(PROGRAMADA) ---"
                )

                pendientes = (
                    FuncionalReportes.filtrar_programadas(
                        citas_db
                    )
                )

                if not pendientes:
                    print("No hay citas pendientes.")

                else:
                    for c in pendientes:
                        print(
                            f" * [ID: {c.id_c}] "
                            f"Fecha: {c.fecha} | "
                            f"Paciente: {c.paciente.nombre}"
                        )


            # ==========================================
            # OPCIÓN 5 - LISTADO DE PACIENTES
            # ==========================================

            elif opcion == "5":

                print(
                    "\n--- LISTADO ANÓNIMO DE PACIENTES "
                    "(LEY N.° 29733) ---"
                )

                resumen = (
                    FuncionalReportes.mapear_resumen(
                        pacientes_db
                    )
                )

                if not resumen:
                    print("No hay pacientes registrados.")

                else:
                    for item in resumen:
                        print(
                            f" * ID: {item['ID']} | "
                            f"Nombre: {item['Nombre']} | "
                            f"DNI Protegido: "
                            f"{item['DNI_Protegido']} | "
                            f"Edad: {item['Edad']} años"
                        )


            # ==========================================
            # OPCIÓN 6 - PROMEDIO DE EDAD
            # ==========================================

            elif opcion == "6":

                print(
                    "\n--- EDAD PROMEDIO DE PACIENTES ---"
                )

                promedio = (
                    FuncionalReportes.promedio_edad(
                        pacientes_db
                    )
                )

                print(
                    f"El promedio de edad de los "
                    f"pacientes registrados es: "
                    f"{promedio:.1f} años"
                )


            # ==========================================
            # OPCIÓN 7 - SALIR
            # ==========================================

            elif opcion == "7":

                print(
                    "\nGracias por usar el sistema del "
                    "Centro de Salud Rural 'Santa Rosa'. "
                    "¡Hasta luego!"
                )

                break


            else:
                print(
                    "❌ Opción no válida. "
                    "Ingrese un número entre 1 y 7."
                )


        except ValidacionError as err:
            print(
                f"❌ [Error de Validación]: {err}"
            )

        except ValueError:
            print(
                "❌ [Error de Dato]: "
                "Debe ingresar un valor numérico válido."
            )


if __name__ == "__main__":
    iniciar_sistema()
