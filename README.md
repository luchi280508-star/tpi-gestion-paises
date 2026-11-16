# Gestión de Datos de Países en Python

Trabajo Práctico Integrador de Programación 1 · Tecnicatura Universitaria en Programación a Distancia · Universidad Tecnológica Nacional.

Esta aplicación de consola permite registrar países, actualizar su población y superficie, buscar por nombre, filtrar registros, ordenarlos y calcular estadísticas sobre el conjunto cargado. Guarda las altas y actualizaciones en `paises.csv`, junto al programa.

## Instalación y uso

Descargá el repositorio (en GitHub, **Code → Download ZIP**) y descomprimilo, o clonalo con Git. Abrí una terminal en la carpeta que contiene `tpi_programacion.py`. Necesitás Python 3.10 o superior por el uso de `match`.

```sh
python -m pip install -r requirements.txt
python tpi_programacion.py
```

Si tu sistema usa `python3` o `py`, usá ese comando en ambas líneas. Elegí una opción y presioná Enter después de cada respuesta.

| Opción | Operación | Datos que solicita |
| --- | --- | --- |
| 1 | Agregar un país | Nombre único, población, superficie en km² y continente. |
| 2 | Actualizar | Nombre completo, nueva población y nueva superficie. |
| 3 | Buscar | Nombre completo o parte del nombre. Ignora mayúsculas y conserva las tildes. |
| 4 | Filtrar | Continente, o mínimo y máximo de población o superficie. Incluye ambos límites. |
| 5 | Ordenar | Nombre, población o superficie. Elegí `s` para descendente o `n` para ascendente. |
| 6 | Ver estadísticas | Muestra extremos, promedios y cantidad por continente. |
| 7 | Salir | Finaliza la sesión. |

Ingresá la población en habitantes y la superficie en km² como enteros positivos, sin separadores de miles. Si al cargar el archivo se detectan filas con campos vacíos o números inválidos, el programa permite consultar las filas válidas y bloquea los cambios. Corregí el CSV y reiniciá el programa.

## Datos incluidos

El CSV está codificado en UTF-8. Su encabezado es `nombre,poblacion,superficie,continente`. El dataset de prueba contiene 271 registros, incluido `mamam`. El programa carga 248 y omite 23 por campos vacíos o valores numéricos inválidos. Con este archivo se pueden realizar consultas. Las altas y actualizaciones quedan bloqueadas hasta corregir las filas rechazadas y reiniciar. Las estadísticas incluyen los duplicados y los nombres ficticios que pasan la validación. Tanto el filtro como el conteo por continente agrupan variantes como `América` y `america`. El resumen muestra la primera grafía encontrada.

## Ejemplos de entrada y salida

**Buscar mamam.** Ingresá `3` y después `mamam`. La consola muestra:

```text
mamam
poblacion: 2323333
superficie: 545454 km²
continente: america
```

**Filtrar por superficie exacta.** Ingresá `4` (filtrar), `3` (superficie), `377975` como mínimo y `377975` como máximo. El único resultado es:

```text
{'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'}
```

**Consultar las estadísticas.** Con el CSV inicial, ingresá `6`:

```text
estadisticas
mayor poblacion: Mundo
menor poblacion: ErrorMuchosCampos
promedio de poblacion: 73707555.65
promedio de superficie: 2898895.83
paises por continente:
América : 41
Asia : 50
Europa : 59
Oceanía : 19
África : 65
Amérika : 1
Fantasia : 2
Asia/Europa : 1
Amercia : 1
Euro : 1
Antártida : 1
3 : 1
america del norte : 1
Europa/Asia : 1
Gran Bretaña : 1
Tierra : 1
Tierra Media : 2
```

## Participación de los integrantes

Distribución propuesta, pendiente de confirmación del grupo.

| Integrante | Aporte propuesto |
| --- | --- |
| Luciano Zárate | Carga y guardado del CSV, altas y actualización de países. |
| Martín Velázquez | Búsqueda, filtros y ordenamiento de los registros. |
| Jerónimo Díaz Guiñazú | Estadísticas, pruebas de consola y documentación de los ejemplos. |

## Informe académico y técnico

El [informe en PDF](Informe_TPI.pdf) incluye el marco teórico, el diagrama de flujo, las ejecuciones de ejemplo, las dificultades técnicas, las conclusiones y la bibliografía.
