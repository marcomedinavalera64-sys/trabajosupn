umbral_alerta = 4 

def evaluar_acceso ( usuario, intentos_fallidos, disppositivo_nuevo):
    puntaje_riesgo = 0
    def sumar_riesgo(puntos):
        nonlocal puntaje_riesgo
        puntaje_riesgo += puntos

    if intentos_fallidos >= +3:
        sumar_riesgo(3)

    if disppositivo_nuevo:
        sumar_riesgo(2)

    if puntaje_riesgo >= umbral_alerta:
        decicion = "BLOQUEAR" 

    else:
        decicion ="PERMITIR"

    print (f"usuario: {usuario}")
    print (f"puntaje de riesgo: {puntaje_riesgo}")
    print (f"decisión: {decicion}")

    return decicion

print (f"umbral configurado: {umbral_alerta}")
evaluar_acceso("ana", 4, True)