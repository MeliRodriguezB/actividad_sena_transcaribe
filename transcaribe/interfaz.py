"""
TransCaribeCol - Interfaz / Diseño del Sistema de Nómina
Actividad 3.4

Este módulo contiene los menús, entradas del usuario y presentación de comprobantes. La lógica de cálculo y archivo está en logica.py.
"""

import os
import transcaribe.logica as logica


class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ROJO = "\033[91m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIAN = "\033[96m"
    BLANCO = "\033[97m"
    GRIS = "\033[90m"
    BG_AZUL = "\033[44m"
    BG_CIAN = "\033[46m"


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input(f"\\n{C.GRIS}Presione [ENTER] para volver al menú principal...{C.RESET}")


def solicitar_nombre():
    while True:
        nombre = input(f"{C.CIAN}>> {C.BLANCO}Nombre del trabajador: {C.RESET}").strip()
        try:
            return logica.validar_nombre(nombre)
        except ValueError as error:
            print(f"{C.ROJO}[ERROR] {error}{C.RESET}")


def registrar_empleado():
    print(f"\\n{C.CIAN}╔════════════════════════════════════════════════════════╗{C.RESET}")
    print(f"{C.CIAN}║{C.BOLD}{C.BLANCO}            REGISTRO Y LIQUIDACIÓN DE NÓMINA            {C.RESET}{C.CIAN}║{C.RESET}")
    print(f"{C.CIAN}╚════════════════════════════════════════════════════════╝{C.RESET}")

    nombre = solicitar_nombre()

    print(f"\\n{C.AMARILLO}{C.BOLD}--- TIPO DE PERSONAL ---{C.RESET}")
    print(f"  {C.CIAN}[1]{C.BLANCO} Administrativo{C.RESET}")
    print(f"  {C.CIAN}[2]{C.BLANCO} Operativo{C.RESET}")

    tipo_op = 0
    while tipo_op not in [1, 2]:
        tipo_op = logica.leer_entero_positivo("Seleccione el tipo (1-2): ")

    if tipo_op == 1:
        print(f"\\n{C.GRIS}[Info] Tarifa Hora: $20,000 | Hora Extra: $25,000 | ARL: 0.522%{C.RESET}")
        ht = logica.leer_entero_positivo("Horas trabajadas en el mes (HT): ")
        he = logica.leer_entero_positivo("Horas extras realizadas (HE): ")
        registro = logica.liquidar_administrativo(nombre, ht, he)
    else:
        print(f"\\n{C.AMARILLO}{C.BOLD}--- CARGOS OPERATIVOS ---{C.RESET}")
        print(f"  {C.CIAN}[1]{C.BLANCO} Conductor         {C.GRIS}(Base: 160h | ARL Riesgo II - 1.044%){C.RESET}")
        print(f"  {C.CIAN}[2]{C.BLANCO} Oficios Generales {C.GRIS}(Base: 100h | ARL Riesgo I  - 0.522%){C.RESET}")
        print(f"  {C.CIAN}[3]{C.BLANCO} Vigilancia        {C.GRIS}(Base: 336h | ARL Riesgo IV - 4.350%){C.RESET}")

        cargo_op = 0
        while cargo_op not in [1, 2, 3]:
            cargo_op = logica.leer_entero_positivo("Seleccione el cargo (1-3): ")

        cfg = logica.CONFIG_OPERATIVO[cargo_op]
        print(f"\\n{C.GRIS}[Info] Horas parametrizadas por contrato para {cfg['cargo']}: {C.AMARILLO}{cfg['horas_base']} h{C.RESET}")
        ht = logica.leer_entero_positivo("Confirme o ingrese horas efectivas trabajadas (HT): ")
        registro = logica.liquidar_operativo(nombre, cargo_op, ht)

    mostrar_comprobante(registro)
    return registro


def mostrar_comprobante(r):
    print(f"\\n{C.AZUL}┌────────────────────────────────────────────────────────┐{C.RESET}")
    print(f"{C.AZUL}│{C.BOLD}{C.CIAN}             COMPROBANTE INDIVIDUAL DE PAGO             {C.RESET}{C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}├────────────────────────────────────────────────────────┤{C.RESET}")
    print(f"{C.AZUL}│{C.RESET} {C.BLANCO}Colaborador  :{C.RESET} {C.BOLD}{r['Nombre']:<39}{C.RESET} {C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}│{C.RESET} {C.BLANCO}Tipo / Cargo :{C.RESET} {C.AMARILLO}{r['Tipo']} - {r['Cargo']:<24}{C.RESET} {C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}├────────────────────────────────────────────────────────┤{C.RESET}")
    print(f"{C.AZUL}│{C.BOLD}{C.VERDE} DEVENGADOS                                             {C.RESET}{C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}│{C.RESET} Horas Trabajadas (HT) : {r['HT']:<6} h | {C.VERDE}${r['Salario']:>15,.2f}{C.RESET}    {C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}│{C.RESET} Horas Extras (HE)     : {r['HE']:<6} h | {C.VERDE}${r['TPHE']:>15,.2f}{C.RESET}    {C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}├────────────────────────────────────────────────────────┤{C.RESET}")
    print(f"{C.AZUL}│{C.BOLD}{C.ROJO} DEDUCCIONES Y SEGURIDAD SOCIAL                         {C.RESET}{C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}│{C.RESET} Aporte Salud          :            {C.ROJO}-${r['Salud']:>14,.2f}{C.RESET}    {C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}│{C.RESET} Aporte Pensión        :            {C.ROJO}-${r['Pensión']:>14,.2f}{C.RESET}    {C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}│{C.RESET} Riesgos Laborales ARL :             {C.AMARILLO}${r['ARL']:>14,.2f}{C.RESET}    {C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}├────────────────────────────────────────────────────────┤{C.RESET}")
    print(f"{C.AZUL}│{C.RESET} {C.BOLD}{C.BLANCO}TOTAL NETO A PAGAR    :{C.RESET}        {C.BOLD}{C.VERDE}${r['Total a pagar']:>19,.2f}{C.RESET}    {C.AZUL}│{C.RESET}")
    print(f"{C.AZUL}└────────────────────────────────────────────────────────┘{C.RESET}")


def listar_registros(registros):
    if not registros:
        print(f"\\n{C.AMARILLO}[AVISO] No hay registros procesados en memoria durante esta sesión.{C.RESET}")
        return

    ancho = 122
    print(f"\\n{C.CIAN}╔{'═' * ancho}╗{C.RESET}")
    print(f"{C.CIAN}║{C.BOLD}{C.BLANCO}{'RESUMEN GENERAL DE NÓMINA EN MEMORIA':^{ancho}}{C.RESET}{C.CIAN}║{C.RESET}")
    print(f"{C.CIAN}╠{'═' * ancho}╣{C.RESET}")

    header = (
        f"{C.CIAN}║{C.RESET} {C.BOLD}{C.AMARILLO}{'Nombre':<16}{C.RESET} {C.GRIS}│{C.RESET} "
        f"{C.BOLD}{C.AMARILLO}{'Tipo':<14}{C.RESET} {C.GRIS}│{C.RESET} "
        f"{C.BOLD}{C.AMARILLO}{'Cargo':<17}{C.RESET} {C.GRIS}│{C.RESET} "
        f"{C.BOLD}{C.AMARILLO}{'HT':>4}{C.RESET} {C.GRIS}│{C.RESET} "
        f"{C.BOLD}{C.AMARILLO}{'Salario':>11}{C.RESET} {C.GRIS}│{C.RESET} "
        f"{C.BOLD}{C.AMARILLO}{'HE':>3}{C.RESET} {C.GRIS}│{C.RESET} "
        f"{C.BOLD}{C.AMARILLO}{'TPHE':>9}{C.RESET} {C.GRIS}│{C.RESET} "
        f"{C.BOLD}{C.AMARILLO}{'Salud':>9}{C.RESET} {C.GRIS}│{C.RESET} "
        f"{C.BOLD}{C.AMARILLO}{'Pensión':>9}{C.RESET} {C.GRIS}│{C.RESET} "
        f"{C.BOLD}{C.AMARILLO}{'ARL':>8}{C.RESET} {C.GRIS}│{C.RESET} "
        f"{C.BOLD}{C.VERDE}{'Total Pagar':>12}{C.RESET} {C.CIAN}║{C.RESET}"
    )
    print(header)
    print(f"{C.CIAN}╠{'─' * ancho}╣{C.RESET}")

    total_nomina = 0.0
    for r in registros:
        total_nomina += r["Total a pagar"]
        linea = (
            f"{C.CIAN}║{C.RESET} {C.BLANCO}{r['Nombre'][:16]:<16}{C.RESET} {C.GRIS}│{C.RESET} "
            f"{r['Tipo'][:14]:<14} {C.GRIS}│{C.RESET} "
            f"{r['Cargo'][:17]:<17} {C.GRIS}│{C.RESET} "
            f"{r['HT']:>4} {C.GRIS}│{C.RESET} "
            f"${r['Salario']:>10,.0f} {C.GRIS}│{C.RESET} "
            f"{r['HE']:>3} {C.GRIS}│{C.RESET} "
            f"${r['TPHE']:>8,.0f} {C.GRIS}│{C.RESET} "
            f"{C.ROJO}${r['Salud']:>8,.0f}{C.RESET} {C.GRIS}│{C.RESET} "
            f"{C.ROJO}${r['Pensión']:>8,.0f}{C.RESET} {C.GRIS}│{C.RESET} "
            f"{C.AMARILLO}${r['ARL']:>7,.0f}{C.RESET} {C.GRIS}│{C.RESET} "
            f"{C.BOLD}{C.VERDE}${r['Total a pagar']:>11,.0f}{C.RESET} {C.CIAN}║{C.RESET}"
        )
        print(linea)

    print(f"{C.CIAN}╠{'═' * ancho}╣{C.RESET}")
    resumen_pie = f"Registros en sesión: {len(registros)}   |   GRAN TOTAL NÓMINA: ${total_nomina:,.2f}"
    print(f"{C.CIAN}║{C.BOLD}{C.VERDE}{resumen_pie:>{ancho - 1}} {C.RESET}{C.CIAN}║{C.RESET}")
    print(f"{C.CIAN}╚{'═' * ancho}╝{C.RESET}")


def leer_archivo():
    contenido = logica.leer_contenido_archivo()
    if contenido is None:
        print(f"\\n{C.ROJO}[ERROR] El archivo '{logica.ARCHIVO_TXT}' aún no ha sido generado.{C.RESET}")
        return

    print(f"\\n{C.CIAN}╔══════════════════════════════════════════════════════════════════════════════╗{C.RESET}")
    print(f"{C.CIAN}║{C.BOLD}{C.BLANCO}                    CONTENIDO DE 'Registros_Nomina.txt'                       {C.RESET}{C.CIAN}║{C.RESET}")
    print(f"{C.CIAN}╚══════════════════════════════════════════════════════════════════════════════╝{C.RESET}\\n")

    if not contenido:
        print(f"{C.AMARILLO}[AVISO] El archivo existe pero está vacío.{C.RESET}")
    else:
        for i, linea in enumerate(contenido.splitlines()):
            if i == 0:
                print(f"{C.BOLD}{C.AMARILLO}{linea}{C.RESET}")
            elif i == 1:
                print(f"{C.GRIS}{linea}{C.RESET}")
            else:
                print(f"{C.BLANCO}{linea}{C.RESET}")
    print(f"\\n{C.GRIS}{'─' * 80}{C.RESET}")


def menu_principal():
    registros_memoria = []
    registros_sin_guardar = []

    while True:
        print(f"\\n{C.AZUL}╔════════════════════════════════════════════════════════╗{C.RESET}")
        print(f"{C.AZUL}║{C.BG_AZUL}{C.BOLD}{C.BLANCO}       TRANSCARIBECOL S.C.A. - SISTEMA DE NÓMINA        {C.RESET}{C.AZUL}║{C.RESET}")
        print(f"{C.AZUL}╠════════════════════════════════════════════════════════╣{C.RESET}")
        print(f"{C.AZUL}║{C.RESET}  {C.CIAN}[1]{C.BLANCO} Registrar y liquidar nuevo trabajador             {C.AZUL}║{C.RESET}")
        print(f"{C.AZUL}║{C.RESET}  {C.CIAN}[2]{C.BLANCO} Visualizar registros de la sesión  {C.GRIS}({len(registros_memoria):>2} en mem.){C.RESET}   {C.AZUL}║{C.RESET}")
        print(f"{C.AZUL}║{C.RESET}  {C.CIAN}[3]{C.BLANCO} Guardar registros en archivo .TXT  {C.AMARILLO}({len(registros_sin_guardar):>2} pend.){C.RESET}     {C.AZUL}║{C.RESET}")
        print(f"{C.AZUL}║{C.RESET}  {C.CIAN}[4]{C.BLANCO} Leer archivo .TXT guardado                        {C.AZUL}║{C.RESET}")
        print(f"{C.AZUL}║{C.RESET}  {C.ROJO}[5]{C.BLANCO} Salir del sistema                                 {C.AZUL}║{C.RESET}")
        print(f"{C.AZUL}╚════════════════════════════════════════════════════════╝{C.RESET}")

        opcion = input(f"{C.CIAN}>> {C.BOLD}{C.BLANCO}Seleccione una opción (1-5): {C.RESET}").strip()

        if opcion == "1":
            nuevo = registrar_empleado()
            registros_memoria.append(nuevo)
            registros_sin_guardar.append(nuevo)
            pausar()
        elif opcion == "2":
            listar_registros(registros_memoria)
            pausar()
        elif opcion == "3":
            if logica.guardar_archivo(registros_sin_guardar):
                print(f"\\n{C.VERDE}{C.BOLD}[OK] Se exportaron correctamente {len(registros_sin_guardar)} registro(s) a '{logica.ARCHIVO_TXT}'.{C.RESET}")
                registros_sin_guardar.clear()
            else:
                print(f"\\n{C.AMARILLO}[AVISO] No hay registros nuevos pendientes por exportar al archivo.{C.RESET}")
            pausar()
        elif opcion == "4":
            leer_archivo()
            pausar()
        elif opcion == "5":
            if registros_sin_guardar:
                print(f"\\n{C.AMARILLO}[ADVERTENCIA] Tiene {len(registros_sin_guardar)} registro(s) sin guardar en el archivo .TXT.{C.RESET}")
                conf = input(f"{C.CIAN}>> {C.BLANCO}¿Desea guardarlos antes de salir? (s/n): {C.RESET}").strip().lower()
                if conf == "s":
                    if logica.guardar_archivo(registros_sin_guardar):
                        print(f"{C.VERDE}[OK] Registros guardados.{C.RESET}")
            print(f"\\n{C.CIAN}Cerrando sesión en el sistema TransCaribeCol. Hasta pronto.{C.RESET}\\n")
            break
        else:
            print(f"\\n{C.ROJO}[ERROR] Opción '{opcion}' no reconocida. Intente nuevamente.{C.RESET}")


if __name__ == "__main__":
    limpiar_pantalla()
    menu_principal()
