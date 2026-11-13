"""
TransCaribeCol - Lógica del Sistema de Nómina

Este módulo contiene reglas de liquidación, validaciones, organización de registros y operaciones con el archivo TXT.
"""

import os

ARCHIVO_TXT = "Registros_Nomina.txt"

# Constantes de liquidación
VALOR_HORA_ADMIN = 20000.0
VALOR_HORA_EXTRA_ADMIN = 25000.0
ARL_ADMIN_TASA = 0.00522

VALOR_HORA_OPERATIVO = 40000.0
IBC_PORCENTAJE_OPERATIVO = 0.40
SALUD_TASA_OPERATIVO = 0.125
PENSION_TASA_OPERATIVO = 0.160

CONFIG_OPERATIVO = {
    1: {"cargo": "Conductor", "horas_base": 160, "tasa_arl": 0.01044, "riesgo": "Riesgo II (1.044%)"},
    2: {"cargo": "Oficios Generales", "horas_base": 100, "tasa_arl": 0.00522, "riesgo": "Riesgo I (0.522%)"},
    3: {"cargo": "Vigilancia", "horas_base": 336, "tasa_arl": 0.04350, "riesgo": "Riesgo IV (4.350%)"}
}


def leer_entero_positivo(mensaje, input_func=input, output_func=print):
    """Solicita un entero mayor o igual a cero."""
    while True:
        try:
            valor = int(input_func(mensaje))
            if valor >= 0:
                return valor
            output_func("[ERROR] Ingrese un valor numérico mayor o igual a 0.")
        except ValueError:
            output_func("[ERROR] Entrada inválida. Debe ingresar un número entero.")


def validar_nombre(nombre):
    """Devuelve el nombre sin espacios externos; exige que no esté vacío."""
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")
    return nombre


def liquidar_administrativo(nombre, ht, he):
    """Calcula la nómina de un trabajador administrativo."""
    tipo = "Administrativo"
    cargo = "Administrativo"

    salario = ht * VALOR_HORA_ADMIN
    tphe = he * VALOR_HORA_EXTRA_ADMIN
    total_devengado = salario + tphe

    salud = total_devengado * 0.04
    pension = total_devengado * 0.04
    arl = total_devengado * ARL_ADMIN_TASA
    total_pagar = total_devengado - (salud + pension)

    return {
        "Nombre": nombre, "Tipo": tipo, "Cargo": cargo,
        "HT": ht, "Salario": salario, "HE": he, "TPHE": tphe,
        "Salud": salud, "Pensión": pension, "ARL": arl,
        "Total a pagar": total_pagar
    }


def liquidar_operativo(nombre, cargo_op, ht):
    """Calcula la nómina de un trabajador operativo según su cargo."""
    cfg = CONFIG_OPERATIVO[cargo_op]
    tipo = "Operativo"
    cargo = cfg["cargo"]
    he = 0
    tphe = 0.0

    salario = ht * VALOR_HORA_OPERATIVO
    ibc = salario * IBC_PORCENTAJE_OPERATIVO
    salud = ibc * SALUD_TASA_OPERATIVO
    pension = ibc * PENSION_TASA_OPERATIVO
    arl = ibc * cfg["tasa_arl"]
    total_pagar = salario - (salud + pension + arl)

    return {
        "Nombre": nombre, "Tipo": tipo, "Cargo": cargo,
        "HT": ht, "Salario": salario, "HE": he, "TPHE": tphe,
        "Salud": salud, "Pensión": pension, "ARL": arl,
        "Total a pagar": total_pagar
    }


def guardar_archivo(registros_pendientes):
    """Añade los registros pendientes al archivo de nómina."""