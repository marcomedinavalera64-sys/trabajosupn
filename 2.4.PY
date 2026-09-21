def _calcular_riesgo(intentos,dispositivo_nuevo, segundo_factor):
    riesgo = intentos * 15
    if dispositivo_nuevo =="s":
        riesgo=riesgo+30
    if segundo_factor=="N":
        riesgo=riesgo+25
    if riesgo>100:
        riesgo=100
    return riesgo

def _determinar_accion(riesgo):
    if riesgo>=70:
        return "BLOQUEAR Y VERIFICAR"
    elif riesgo>=40:
        return"SOLICITAR VERIFICACION"
    else :
        return "PERMITIR"

def evaluar_acceso(alias, intentos, dispositivos_nuevo,segundo_factor):
    riesgo= _calcular_riesgo(intentos,dispositivos_nuevo,segundo_factor)
    accion=_determinar_accion(riesgo)
    print("/ n RESULTADO DE SEGURIDAD")
    print(f"Alias: {alias}")
    print(f"Riesgo: {riesgo}puntos")
    print(f"Acción: {accion}")


def main():
    alias=input("alias de la cuenta: ")
    intentos=int(input("intentos fallidos: "))
    dispositivo_nuevo=input("¿dispositivo nuevo? (s/n): ")
    segundo_factor=input("¿segundo factor activo? (S/N): ")

    evaluar_acceso(alias, intentos, dispositivo_nuevo, segundo_factor)

    main()
    
