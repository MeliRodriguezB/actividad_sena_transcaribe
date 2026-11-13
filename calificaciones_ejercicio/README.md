# Actividad 3.3. Actividades de Apropiación – Sistema de registro y procesamiento de calificaciones

Aplicación de consola en Python que registra las calificaciones de varios aprendices, calcula el promedio de cada uno, determina si aprobó y muestra el promedio general del grupo. Los resultados se guardan en un archivo CSV.

## ¿Qué hace?

1. Pide la cantidad de aprendices del grupo.
2. Por cada aprendiz, pide el nombre y sus 3 calificaciones (de 0 a 100).
3. Calcula el promedio individual y decide el estado: **Aprobó** si el promedio es mayor o igual a 70, **No aprobó** en caso contrario.
4. Muestra una tabla final con todos los aprendices, el promedio general del grupo y los totales de aprobados y no aprobados.
5. Guarda los resultados en `calificaciones.csv` y, al volver a ejecutar, muestra los registros guardados.

## Estructura del proyecto

| Archivo | Contenido |
| --- | --- |
| `calificaciones.py` | Lógica: lectura y validación de datos, cálculos, decisión de estado y lectura/escritura del CSV. |
| `estilos.py` | Parte visual: colores, títulos, tablas y mensajes en pantalla. No tiene cálculos. |
| `calificaciones.csv` | Se crea solo al ejecutar el programa; guarda los registros procesados. |

## Requisitos

- Python 3.8 o superior. No necesita instalar librerías externas.
- Una terminal con soporte de colores (PowerShell, Terminal de VS Code, etc.).

## Cómo ejecutarlo

Con `calificaciones.py` y `estilos.py` en la misma carpeta:

```
python calificaciones.py
```

## Reglas del problema

| Parámetro | Valor |
| --- | --- |
| Escala de calificación | 0 a 100 |
| Calificaciones por aprendiz | 3 |
| Promedio para aprobar | 70 o más (el 70 exacto aprueba) |
| Cantidad de aprendices | Entero mayor o igual a 1 |

Los datos se validan: se rechazan cantidades menores a 1, nombres vacíos, notas fuera de rango y entradas que no sean numéricas. En cada caso el programa muestra el error y vuelve a pedir el dato.

Las constantes (`NUM_NOTAS`, `NOTA_MIN`, `NOTA_MAX`, `PROMEDIO_APROBACION`) están al inicio de `calificaciones.py` y se pueden cambiar sin tocar el resto del código.

## Fórmulas

- Promedio del aprendiz = suma de sus notas / 3
- Promedio general = suma de los promedios de todos los aprendices / cantidad de aprendices

La decisión de aprobar usa el promedio sin redondear; los decimales solo se redondean al mostrarlos en pantalla.

## Ejemplo de ejecución

Datos: Ana (80, 90, 70), Luis (60, 65, 70) y Marta (70, 70, 70).

```
No.  Nombre          Nota 1  Nota 2  Nota 3  Promedio  Estado
──────────────────────────────────────────────────────────────
1    Ana             80.0    90.0    70.0    80.00     ✔ Aprobó
2    Luis            60.0    65.0    70.0    65.00     ✖ No aprobó
3    Marta           70.0    70.0    70.0    70.00     ✔ Aprobó
──────────────────────────────────────────────────────────────

Promedio general del grupo: 71.67
Aprobados: 2  |  No aprobados: 1
```

## Pruebas de escritorio

| Prueba | Datos | Promedio general | Aprobados | No aprobados |
| --- | --- | --- | --- | --- |
| Datos sugeridos | A (promedio 85), B (65), C (70) | 73.33 | 2 | 1 |
| Caso normal | Ana, Luis, Marta (ejemplo anterior) | 71.67 | 2 | 1 |
| Valores extremos | 100, 100, 100 y 0, 0, 0 | 50.00 | 1 | 1 |
| Límite | 70, 70, 69 y 69, 70, 71 | 69.83 | 1 | 1 |
| Un solo aprendiz | 75, 80, 85 | 80.00 | 1 | 0 |
| Todos reprueban | 50, 60, 40 y 65, 68, 62 | 57.50 | 0 | 2 |

## Persistencia en CSV

- El archivo `calificaciones.csv` se crea junto al programa la primera vez que se ejecuta.
- Cada ejecución agrega los aprendices nuevos al final, sin borrar los anteriores.
- Columnas: `fecha`, `nombre`, `nota_1`, `nota_2`, `nota_3`, `promedio`, `estado`.
- El separador es `;` para que Excel en español lo abra directamente en columnas. Se puede cambiar en la constante `SEPARADOR`.

## Conceptos aplicados

- Ciclos anidados (`for`): uno recorre a los aprendices y otro lee las notas de cada uno.
- Estructura de decisión (`if / else`) para determinar el estado.
- Arreglos (listas) para guardar nombres, notas, promedios y estados.
- Acumuladores y contadores para el promedio general y los totales.
- Validación de datos de entrada.
- Separación de lógica y presentación en dos archivos.
- Persistencia de datos con archivos CSV.