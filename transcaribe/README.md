    # TransCaribeCol --- Sistema de liquidación de nómina

Aplicación de consola desarrollada en Python para registrar trabajadores
y realizar liquidaciones de nómina según el tipo de trabajador:
administrativo u operativo.

## Características

-   Menú de consola para navegar por las opciones del sistema.
-   Registro de trabajadores administrativos y operativos.
-   Liquidación de nómina según el tipo de trabajador.
-   Visualización del comprobante de liquidación.
-   Consulta de registros de la sesión.
-   Guardado y lectura de información desde un archivo de texto.
-   Separación entre interfaz y lógica del programa para facilitar el
    mantenimiento.

## Estructura del proyecto

``` text
TransCaribeCol/
├── interfaz.py   # Menús, entradas del usuario y presentación de resultados
├── logica.py     # Validaciones, cálculos y manejo de archivos
└── README.md     # Documentación del proyecto
```

> Los archivos `interfaz.py` y `logica.py` deben permanecer en la misma
> carpeta para que la importación de la lógica funcione correctamente.

## Requisitos

-   Python 3.10 o una versión compatible.
-   No requiere instalar paquetes externos si se utiliza únicamente la
    biblioteca estándar de Python.

## Ejecución

1.  Descarga o copia `interfaz.py` y `logica.py` en una misma carpeta.

2.  Abre una terminal en esa carpeta.

3.  Ejecuta:

    ``` bash
    python interfaz.py
    ```

En Windows también puedes utilizar:

``` powershell
py interfaz.py
```

## Uso general

1.  Inicia el programa.
2.  Selecciona una opción del menú principal.
3.  Registra los datos solicitados del trabajador.
4.  Selecciona o confirma el tipo de trabajador y los datos requeridos
    para la liquidación.
5.  Revisa el comprobante generado.
6.  Consulta los registros de la sesión o guarda la información cuando
    corresponda.
7.  Utiliza la opción de salida para cerrar el programa.

## Archivos de datos

El sistema utiliza un archivo de texto para almacenar y consultar las
liquidaciones. El archivo se crea o actualiza desde las opciones de
guardado del programa.

Mantén una copia de seguridad de los archivos de datos si necesitas
conservar el historial de liquidaciones.

## Organización del código

### `interfaz.py`

Contiene los elementos relacionados con la interacción con el usuario:

-   Menú principal y submenús.
-   Solicitud y presentación de datos.
-   Mensajes y comprobantes.
-   Visualización de registros.
-   Llamadas a las funciones de `logica.py`.

### `logica.py`

Contiene las funciones de procesamiento:

-   Validación de datos.
-   Cálculos de liquidación para trabajadores administrativos.
-   Cálculos de liquidación para trabajadores operativos.
-   Lectura y escritura del archivo de registros.
-   Parámetros y constantes utilizados en los cálculos.

## Notas

-   Verifica que los datos ingresados sean correctos antes de guardar
    una liquidación.
-   Los cálculos corresponden a las reglas implementadas en el código
    del proyecto.
-   Para modificar las fórmulas de nómina, realiza los cambios en
    `logica.py`.
-   Para modificar menús, textos o la presentación, realiza los cambios
    en `interfaz.py`.

    
