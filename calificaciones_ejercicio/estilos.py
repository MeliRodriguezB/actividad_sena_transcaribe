"""
estilos.py - Parte VISUAL del sistema de calificaciones.

Aquí solo hay colores y formato de salida. No hay cálculos ni decisiones
de negocio: eso vive en calificaciones.py.
"""

import os

# Truco para que los colores también funcionen en la consola de Windows
os.system("")

# ---------------------------------------------------------------
# CÓDIGOS DE COLOR (ANSI). Se escriben antes del texto y RESET lo cierra.
# ---------------------------------------------------------------
RESET = "\033[0m"
NEGRITA = "\033[1m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
CYAN = "\033[96m"
GRIS = "\033[90m"

ANCHO = 62  # Ancho de las líneas decorativas


# ---------------------------------------------------------------
# ENCABEZADOS
# ---------------------------------------------------------------
def titulo(texto):
    """Muestra un título grande entre líneas."""
    print(f"\n{CYAN}{NEGRITA}{'═' * ANCHO}")
    print(texto.center(ANCHO))
    print(f"{'═' * ANCHO}{RESET}")


def subtitulo(texto):
    """Muestra el encabezado de cada aprendiz."""
    print(f"\n{AZUL}{NEGRITA}── {texto} {'─' * (ANCHO - len(texto) - 4)}{RESET}")


# ---------------------------------------------------------------
# MENSAJES Y PREGUNTAS
# ---------------------------------------------------------------
def pedir(texto):
    """Pide un dato al usuario con el texto en color."""
    return input(f"{AMARILLO}{texto}{RESET}")


def error(texto):
    """Muestra un mensaje de error en rojo."""
    print(f"{ROJO}✖ {texto}{RESET}")


# ---------------------------------------------------------------
# RESULTADOS
# ---------------------------------------------------------------
def color_estado(estado):
    """Devuelve el estado en verde si aprobó o en rojo si no."""
    if estado == "Aprobó":
        return f"{VERDE}{NEGRITA}✔ {estado}{RESET}"
    return f"{ROJO}{NEGRITA}✖ {estado}{RESET}"


def mostrar_resumen_aprendiz(nombre, promedio, estado):
    """Resumen corto que se muestra al terminar cada aprendiz."""
    print(f"{GRIS}Promedio de {nombre}:{RESET} {NEGRITA}{promedio:.2f}{RESET}  "
          f"{color_estado(estado)}")


def mostrar_tabla(nombres, notas, promedios, estados):
    """Muestra la tabla final con todos los aprendices."""
    cantidad_notas = len(notas[0])

    # Encabezado de la tabla (el relleno se hace ANTES de poner el color)
    encabezado = f"{'No.':<5}{'Nombre':<16}"
    for j in range(cantidad_notas):
        encabezado += f"{'Nota ' + str(j + 1):<8}"
    encabezado += f"{'Promedio':<10}Estado"
    print(f"{NEGRITA}{CYAN}{encabezado}{RESET}")
    print(f"{GRIS}{'─' * ANCHO}{RESET}")

    # Una fila por aprendiz
    for i in range(len(nombres)):
        fila = f"{i + 1:<5}{nombres[i]:<16}"
        for nota in notas[i]:
            fila += f"{nota:<8.1f}"
        fila += f"{promedios[i]:<10.2f}"
        print(fila + color_estado(estados[i]))

    print(f"{GRIS}{'─' * ANCHO}{RESET}")

def mostrar_resumen_grupo(promedio_general, aprobados, no_aprobados):
    """Muestra el promedio general y los totales del grupo."""
    # El promedio general se pinta según supere o no el mínimo de aprobación
    print(f"\n{NEGRITA}Promedio general del grupo: {AMARILLO}{promedio_general:.2f}{RESET}")
    print(f"{VERDE}Aprobados: {aprobados}{RESET}  {GRIS}|{RESET}  "
          f"{ROJO}No aprobados: {no_aprobados}{RESET}\n")
    
