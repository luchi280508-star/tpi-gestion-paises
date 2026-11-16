import csv
import os
import unicodedata
try:
    from colorama import Style, Fore, Back, init
    init(autoreset=True)
except ImportError:
    class _Color:
        def __getattr__(self, name):
            return ""
    Style = Fore = Back = _Color()


def cargar_paises(archivo_csv):
    paises = []
    hay_errores = False
    try:
        with open(archivo_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if not all(isinstance(fila.get(campo), str) and fila[campo].strip()
                    for campo in ["nombre", "poblacion", "superficie", "continente"]):
                    print(Fore.RED + "error en esta fila:", fila)
                    print(Fore.RED + "error hay campos vacios o faltantes")
                    continue
                try:
                    poblacion = int(fila["poblacion"])
                    superficie = int(fila["superficie"])
                    if poblacion <= 0 or superficie <= 0:
                        print(Fore.RED + "error valores numericos invalidos en:", fila.get("nombre", ""))
                        continue
                except ValueError:
                    print(Fore.RED + "error poblacion o superficie invalida en:", fila.get("nombre", ""))
                    continue
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": fila["continente"].strip()}
                paises.append(pais)
    except FileNotFoundError:
        print(Fore.RED + "no existe el archivo csv, se iniciara una lista vacia")
    except OSError as error:
        print(Fore.RED + "error no se pudo leer el archivo:", error)
        hay_errores = True
    return paises, hay_errores


def agregar_pais(paises, nombre, poblacion, superficie, continente):
    if not nombre.strip() or not continente.strip():
        return "invalido"
    for pais in paises:
        if pais["nombre"].strip().lower() == nombre.strip().lower():
            return "duplicado"
    try:
        poblacion = int(poblacion)
        superficie = int(superficie)
        if poblacion <= 0 or superficie <= 0:
            return "invalido"
    except ValueError:
        return "invalido"
    nuevo_pais = {
        "nombre": nombre.strip(),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente.strip()
    }
    paises.append(nuevo_pais)
    return "agregado"


def actualizar_datos(paises, nombre, nueva_poblacion, nueva_superficie):
    for pais in paises:
        if pais["nombre"].lower() == nombre.strip().lower():
            try:
                nueva_poblacion = int(nueva_poblacion)
                nueva_superficie = int(nueva_superficie)
            except ValueError:
                return "no_numerico"
            if nueva_poblacion <= 0 or nueva_superficie <= 0:
                return "valor_invalido"
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            return "actualizado"
    return "no_encontrado"


def buscar_pais(paises, busqueda):
    resultado = []
    if not busqueda.strip():
        return []
    else:
        for pais in paises:
            if busqueda.lower().strip() in pais["nombre"].lower():
                resultado.append(pais)
        return resultado


def normalizar(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caracter for caracter in texto
        if unicodedata.category(caracter) != "Mn")
    return texto


def filtrar_continente(paises, continente):
    resultados = []
    for pais in paises:
        if normalizar(pais["continente"]) == normalizar(continente):
            resultados.append(pais)
    return resultados


def filtrar_poblacion(paises, minimo, maximo):
    resultados = []
    if minimo > maximo:
        return None
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)
    return resultados


def filtrar_superficie(paises, minimo, maximo):
    resultados = []
    if minimo > maximo:
        return None
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)
    return resultados


def ordenar_paises(paises, descendente = False):
    return sorted(paises, key=lambda pais: pais["nombre"].lower(), reverse=descendente)


def ordenar_poblacion(paises, descendente = False):
    return sorted(paises, key=lambda pais: pais["poblacion"], reverse=descendente)


def ordenar_superficie(paises, descendente = False):
    return sorted(paises, key=lambda pais: pais["superficie"], reverse=descendente)


def mayor_menor_poblacion(paises):
    if len(paises) == 0:
        return None
    mayor = max (paises, key=lambda pais: pais["poblacion"])
    menor = min (paises, key=lambda pais: pais["poblacion"])
    return mayor, menor


def promedio_de_poblacion(paises):
    if len(paises) == 0:
        return None
    suma = 0
    for pais in paises:
        suma += pais["poblacion"]
    promedio = suma / len(paises)
    return promedio


def promedio_de_superficie(paises):
    if len(paises) == 0:
        return None
    suma = 0
    for pais in paises:
        suma += pais["superficie"]
    promedio = suma / len(paises)
    return promedio


def contar_paises_por_continente(paises):
    cantidades = {}
    nombres = {}
    for pais in paises:
        continente = pais["continente"].strip()
        clave = normalizar(continente)
        if clave in cantidades:
            cantidades[clave] += 1
        else:
            cantidades[clave] = 1
            nombres[clave] = continente.capitalize()
    resultado = {}
    for clave, cantidad in cantidades.items():
        resultado[nombres[clave]] = cantidad
    return resultado


def guardar_paises(paises, archivo_csv):
    encabezado = ["nombre", "poblacion", "superficie", "continente"]
    try:
        with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=encabezado)
            escritor.writeheader()
            escritor.writerows(paises)
        return True
    except OSError as error:
        print(Fore.RED + "error al guardar el archivo:" ,error)
        return False


def mostrar_menu():
    print (Back.BLUE + "1. agregar un pais")
    print (Back.BLUE + "2. actualizar info de un pais")
    print (Back.BLUE + "3. buscar un pais")
    print (Back.BLUE + "4. filtrar paises")
    print (Back.BLUE + "5. ordenar paises")
    print (Back.BLUE + "6. mostrar estadisticas")
    print (Back.BLUE + "7. salir")


def menu_principal():

    ruta_csv = os.path.join(os.path.dirname(__file__), "paises.csv")
    paises, hay_errores = cargar_paises(ruta_csv)
    while True:
        mostrar_menu()
        opcion = input (Fore.BLUE + "seleccione una opcion 1/7: ")
        match opcion:
            case "1":
                if hay_errores:
                    print(Fore.RED + "no se pueden guardar cambios corrija primero el archivo CSV")
                else:
                    nombre = input(Fore.RED + "ingrese el nombre del pais: ")
                    poblacion = input (Fore.YELLOW + "ingrese la poblacion: ")
                    superficie = input (Fore.YELLOW + "ingrese la superficie: ")
                    continente = input (Fore.YELLOW + "ingrese el continente: ")
                    resultado = agregar_pais(paises, nombre, poblacion, superficie, continente)
                    if resultado == "agregado":
                        if guardar_paises(paises, ruta_csv):
                            print(Fore.GREEN + "pais agregado correctamente")
                        else:
                            print(Fore.RED + "error al guardar los cambios")
                    elif resultado == "duplicado":
                        print(Fore.RED + "error el pais ya existe")
                    elif resultado == "invalido":
                        print(Fore.RED + "error datos invalidos")
            case "2":
                if hay_errores:
                    print(Fore.RED + "no se pueden guardar cambios corrija primero el archivo CSV")
                else:
                    nombre1 = input(Back.BLUE + "ingrese el pais que desea actualizar: ")
                    poblacion1 = input(Back.BLUE + "ingrese la nueva poblacion: ")
                    superficie1 = input(Back.BLUE + "ingrese la nueva superficie: ")
                    resultado1 = actualizar_datos(paises, nombre1, poblacion1, superficie1)
                    if resultado1 == "actualizado":
                        if guardar_paises(paises, ruta_csv):
                            print (Fore.GREEN + "pais actualizado correctamente")
                        else:
                            print (Fore.RED + "error al guardar los cambios")
                    elif resultado1 == "no_encontrado":
                        print (Fore.RED + "el pais no existe")
                    elif resultado1 == "no_numerico":
                        print (Fore.RED + "la población y la superficie deben ser numeros")
                    elif resultado1 == "valor_invalido":
                        print (Fore.RED + "la población y la superficie deben ser mayores a cero")
            case "3":
                nombre = input(Back.BLUE + "ingrese el nombre del pais: ")
                resultados = buscar_pais(paises, nombre)
                if len(resultados) != 0:
                    for pais in resultados:
                        print (Fore.RED + pais['nombre'])
                        print (Fore.YELLOW + "poblacion:", pais['poblacion'])
                        print (Fore.YELLOW + "superficie:", pais['superficie'], "km²")
                        print (Fore.YELLOW + "continente:", pais['continente'])
                else:
                    print(Fore.RED + "no se encontraron paises")
            case "4":
                print (Fore.RED + "como desea filtrar los paises: ")
                print (Fore.YELLOW + "1. por continente")
                print (Fore.YELLOW + "2. por poblacion")
                print (Fore.YELLOW + "3. por superficie")
                filtro = input (Back.BLUE + "ingrese una opcion 1/3: ")
                if filtro == "1":
                    continente = input(Fore.YELLOW + "Ingrese el continente: ")
                    resultados = filtrar_continente(paises, continente)
                elif filtro == "2":
                    try:
                        minimo = int(input(Fore.YELLOW + "Población mínima: "))
                        maximo = int(input(Fore.YELLOW + "Población máxima: "))
                        if minimo <= 0 or maximo <= 0 or minimo > maximo:
                            resultados = None
                        else:
                            resultados = filtrar_poblacion(paises, minimo, maximo)
                    except ValueError:
                        resultados = None
                elif filtro == "3":
                    try:
                        minimo1 = int (input (Fore.YELLOW + "superficie minima: "))
                        maximo1 = int (input (Fore.YELLOW + "superficie maxima: "))
                        if minimo1 <= 0 or maximo1 <= 0 or minimo1 > maximo1:
                            resultados = None
                        else:
                            resultados = filtrar_superficie(paises, minimo1, maximo1)
                    except ValueError:
                        resultados = None
                else:
                    resultados = None
                if resultados is None:
                    print(Fore.RED + "filtro invalido. verifique los valores ingresados")
                elif len(resultados) == 0:
                    print(Fore.RED + "no se encontraron paises")
                else:
                    for pais in resultados:
                        print(Fore.GREEN + pais["nombre"])
                        print(Fore.YELLOW + "poblacion:", pais["poblacion"])
                        print(Fore.YELLOW + "superficie:", pais["superficie"], "km²")
                        print(Fore.YELLOW + "continente:", pais["continente"])
            case "5":
                print (Fore.RED + "como desea ordenar los paises: ")
                print (Fore.YELLOW + "1. por nombre")
                print (Fore.YELLOW + "2. por poblacion")
                print (Fore.YELLOW + "3. por superficie")
                criterio = input (Back.BLUE + "seleccione una opcion 1/3: ")
                sentido = input (Back.BLUE + "orden descendente? (s/n): ").lower().strip()
                if sentido not in ["s", "n"]:
                    print (Fore.RED + "sentido invalido")
                else:
                    descendente = sentido == "s"
                    if criterio == "1":
                        resultados = ordenar_paises(paises, descendente)
                    elif criterio == "2":
                        resultados = ordenar_poblacion(paises, descendente)
                    elif criterio == "3":
                        resultados = ordenar_superficie(paises, descendente)
                    else:
                        resultados = None
                    if resultados is None:
                        print (Fore.RED + "criterio invalido")
                    else:
                        for pais in resultados:
                            print(Fore.GREEN + pais["nombre"])
                            print(Fore.YELLOW + "poblacion:", pais["poblacion"])
                            print(Fore.YELLOW + "superficie:", pais["superficie"], "km²")
                            print(Fore.YELLOW + "continente:", pais["continente"])
            case "6":
                resultado = mayor_menor_poblacion(paises)
                if resultado is None:
                    print (Fore.RED + "no hay paises cargados")
                else:
                    mayor, menor = resultado
                    print (Fore.RED + "estadisticas")
                    print (Fore.YELLOW + "mayor poblacion:", mayor["nombre"])
                    print (Fore.YELLOW + "menor poblacion:", menor["nombre"])
                    print (Fore.YELLOW + "promedio de poblacion:", round(promedio_de_poblacion(paises), 2))
                    print (Fore.YELLOW + "promedio de superficie:", round(promedio_de_superficie(paises), 2))
                    cantidades = contar_paises_por_continente(paises)
                    print (Fore.GREEN + "paises por continente:")
                    for continente, cantidad in cantidades.items():
                        print(Fore.YELLOW + continente, ":", cantidad)
            case "7":
                print ("saliendo")
                break
            case _:
                print (Fore.RED + "opcion invalida")


if __name__ == "__main__":
    menu_principal()