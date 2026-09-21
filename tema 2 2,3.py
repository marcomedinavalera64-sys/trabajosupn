umbral_latencia = 120 

def generar_reporte(latencia1, latencia2, latencia3 ):
    servicios_degradados = 0 

    def evaluar (latencia):
        nonlocal servicios_degradados 
        if latencia > umbral_latencia:
            servicios_degradados += 1

    evaluar(latencia1)
    evaluar(latencia2)
    evaluar(latencia3)

    return servicios_degradados

total_degradados = generar_reporte(95, 160, 135)

print (f"umbral local: {umbral_latencia} ms")
print (f"servicios degradados: {total_degradados}")
