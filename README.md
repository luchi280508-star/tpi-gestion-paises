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

El CSV está codificado en UTF-8. Su encabezado es `nombre,poblacion,superficie,continente`. Incluye Argentina, Japón, Brasil y un cuarto registro denominado `mamam`. Se conserva el archivo recibido como dataset de práctica. Los resultados describen esas cuatro filas. El filtro por continente reúne `América` y `america`, mientras que el conteo estadístico las muestra por separado porque usa el texto original.

## Ejemplos de entrada y salida

**Buscar Argentina.** Ingresá `3` y después `arg`. La consola muestra:

```text
Argentina
poblacion: 45376763
superficie: 2780400 km²
continente: América
```

**Filtrar por superficie exacta.** Ingresá `4` (filtrar), `3` (superficie), `377975` como mínimo y `377975` como máximo. El único resultado es:

```text
{'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'}
```

**Consultar las estadísticas.** Con el CSV inicial, ingresá `6`:

```text
estadisticas
mayor poblacion: Brasil
menor poblacion: mamam
promedio de poblacion: 96873383.25
promedio de superficie: 3054899.0
paises por continente:
América : 2
Asia : 1
america : 1
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
