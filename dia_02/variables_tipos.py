# ================================================
# Dia 2 - Varibles y Tipos de Datos
# Contexto: laboratorio de bioinformatica
#=================================================


# --- INT: numeros enteros ---
colonias_placa_a = 142          # conteo de colonias de placa A
colonias_placa_b = 89           # conteo de colonias de placa B
total_colonias = colonias_placa_a + colonias_placa_b

print("Total de colonias:", total_colonias)
print("Tipo de dato:", type(total_colonias))


# --- FLOAT: numeros decimales ---
concentracion_adn = 52.4            # ng/uL medido por nanodrop
volumen_muestra = 1.5               # mL

masa_total = concentracion_adn * volumen_muestra

print("\nMasa total de ADN:", masa_total, "ng")
print("Tipo de dato:", type(masa_total))


# --- STR: texto ---
secuencia_primer = "ATCGGCTA"
gen_objetivo = "BRCA1"
descripcion = f"Gen {gen_objetivo} aplificado con primer {secuencia_primer}"

print("\nDescripcion:", descripcion)
print("Tipo de dato:", type(secuencia_primer))


# --- BOOL: verdadero o falso ---
pureza_260_280 = 1.85           # ratio aceptable 1.8 y 2.0
muestra_pura = 1.8 <= pureza_260_280 <= 2.0

print("\nMuestra pura?:", muestra_pura)
print("Tipo de dato:", type(muestra_pura))


# ================================================
# CONVERSIONES ENTRE TIPOS DE DATOS (casting)
#=================================================

# --- problema real: datos que llegan como texto
colonias_texto = "142"          # viene de leer un archivo CSV
factor_dilucion = "2.5"         # viene de un input del usuario

# Verificamos los tipos de originales
print("\nTipo original colonias_texto:", type(colonias_texto))
print("Tipo original factor_dilucion:", type(factor_dilucion))

# --- conversion para operar ---
colonias_int = int(colonias_texto)
factor_float = float(factor_dilucion)

colonias_reales = colonias_int * factor_float
print("Tipo de dato de respuesta:", type(colonias_reales))

# --- De numero a texto ---
reporte = "Resultado del conteo: " + str(colonias_reales)
print(reporte)

# --- Riesgo real: conversion imposible ---
try:
    valor_invalido = int("ATCG")
except ValueError as e:
    print("/Error de conversión:", e)
    print("no podes convertir una secuencia de ADN a entero")    


# ===============================================
# OPERADORES ARITMETICOS Y DE ASIGNACION
# ===============================================

# --- Aritmeticos ---
a = 10
b = 3

print("\nSuma:",            a + b)
print("Resta:",             a - b)
print("Multiplicacion:",    a * b)
print("Division:",          a / b)    # siempre devuelve float
print("Division entera:",   a // b)   # devuelve entero
print("Modulo:",            a % b)    # resto de la division
print("Potencia",           a ** b)   # 10°3

# --- De asignacion ---
conteo = 0
conteo += 1     # equivale a conteo = conteo + 1
print("\nConteo tras += 1:", conteo)

conteo *= 5     # equivalente a conteo = conteo * 5
print("conteo tras *= 5", conteo)

# --- Aplicado a biotecnologia ---
volumen_total = 50      # uL de reaccion PCR
volumen_adn = 5         # uÑ de DN templante
porcentaje_adn = (volumen_adn / volumen_total) * 100

print(f"\nEl ADN representa el {porcentaje_adn}% de la reaccion")