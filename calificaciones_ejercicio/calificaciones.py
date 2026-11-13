"""
Actividad 3.3 - Sistema de registro y procesamiento de calificaciones.

Este archivo contiene SOLO la lógica: lectura de datos, cálculos y decisiones.
Todo lo visual (colores, tablas, mensajes) está en estilos.py.

Para ejecutar:  python calificaciones.py   (ambos archivos en la misma carpeta)
"""

import calificaciones_ejercicio.estilos as ui  # Parte visual

# ---------------------------------------------------------------
# CONSTANTES (valores fijos del problema)
# ---------------------------------------------------------------
NUM_NOTAS = 3               # Cantidad de calificaciones por aprendiz
NOTA_MIN = 0                # Nota mínima válida
NOTA_MAX = 100              # Nota máxima válida
PROMEDIO_APROBACION = 70    # Con este promedio o más, el aprendiz aprueba


# ---------------------------------------------------------------
# FUNCIONES PARA LEER Y VALIDAR DATOS
# ---------------------------------------------------------------
def leer_cantidad_aprendices():
    """Pide la cantidad de aprendices hasta que sea un entero >= 1."""
    while True:
        try:
            cantidad = int(ui.pedir("¿Cuántos aprendices tiene el grupo?: "))
            if cantidad >= 1:
                return cantidad
            ui.error("Debe haber al menos 1 aprendiz.")
        except ValueError:
            ui.error("Entrada inválida. Ingrese un número entero.")


def leer_nombre():
    """Pide el nombre hasta que no esté vacío."""
    nombre = ui.pedir("Nombre del aprendiz: ").strip()
    while nombre == "":
        ui.error("El nombre no puede estar vacío.")
        nombre = ui.pedir("Nombre del aprendiz: ").strip()
    return nombre


def leer_nota(numero):
    """Pide una nota hasta que sea un número entre NOTA_MIN y NOTA_MAX."""
    while True:
        try:
            nota = float(ui.pedir(f"  Nota {numero}: "))
            if NOTA_MIN <= nota <= NOTA_MAX:
                return nota
            ui.error(f"Nota inválida: ingrese un valor entre {NOTA_MIN} y {NOTA_MAX}.")
        except ValueError:
            ui.error("Entrada inválida. Ingrese un número.")


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------
def main():
    ui.titulo("SISTEMA DE REGISTRO DE CALIFICACIONES")

    # Acumuladores y contadores (empiezan en 0)
    acumulado_promedios = 0
    aprobados = 0
    no_aprobados = 0

    # Cantidad de aprendices del grupo
    n_aprendices = leer_cantidad_aprendices()

    # Arreglos (listas) donde se guardan los datos de todos los aprendices
    nombres = []     # nombre de cada aprendiz
    notas = []       # matriz: cada elemento es la lista de notas de un aprendiz
    promedios = []   # promedio de cada aprendiz
    estados = []     # "Aprobó" o "No aprobó" de cada aprendiz

    # CICLO EXTERNO: se repite una vez por cada aprendiz
    for i in range(n_aprendices):
        ui.subtitulo(f"Aprendiz {i + 1} de {n_aprendices}")
        nombre = leer_nombre()

        # La suma se reinicia en 0 con cada aprendiz
        suma_notas = 0
        notas_aprendiz = []

        # CICLO INTERNO: lee las NUM_NOTAS calificaciones del aprendiz
        for j in range(NUM_NOTAS):
            nota = leer_nota(j + 1)
            notas_aprendiz.append(nota)
            suma_notas = suma_notas + nota

        # Promedio del aprendiz (sin redondear, para decidir con exactitud)
        promedio = suma_notas / NUM_NOTAS

        # ESTRUCTURA DE DECISIÓN: aprueba si el promedio es >= 70
        if promedio >= PROMEDIO_APROBACION:
            estado = "Aprobó"
            aprobados = aprobados + 1
        else:
            estado = "No aprobó"
            no_aprobados = no_aprobados + 1

        # Se guardan los datos en los arreglos (misma posición = mismo aprendiz)
        nombres.append(nombre)
        notas.append(notas_aprendiz)
        promedios.append(promedio)
        estados.append(estado)

        # Se suma el promedio al acumulado del grupo
        acumulado_promedios = acumulado_promedios + promedio

        # Resumen individual
        ui.mostrar_resumen_aprendiz(nombre, promedio, estado)

    # Promedio general del grupo
    promedio_general = acumulado_promedios / n_aprendices

    # Resultados finales
    ui.titulo("RESULTADOS DEL GRUPO")
    ui.mostrar_tabla(nombres, notas, promedios, estados)
    ui.mostrar_resumen_grupo(promedio_general, aprobados, no_aprobados)


# Punto de entrada: ejecuta el programa al correr el archivo
if __name__ == "__main__":
    main()
    

