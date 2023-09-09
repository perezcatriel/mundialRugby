import csv
import os
from datetime import datetime

# Función para obtener un nuevo ID automático
def obtener_nuevo_id(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return 1

    with open(nombre_archivo, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        last_row = None
        for row in reader:
            last_row = row
        if last_row:
            return int(last_row["ID"]) + 1
        else:
            return 1

def ingresar_partido(paises_participantes):
    # Obtener un nuevo ID automático para el partido
    nuevo_id = obtener_nuevo_id(nombre_archivo_csv)

    while True:
        equipo_local = input("Equipo local: ").capitalize()
        equipo_visitante = input("Equipo visitante: ").capitalize()

        if any(pais["pais"] == equipo_local for pais in paises_participantes) and any(
                pais["pais"] == equipo_visitante for pais in paises_participantes):
            break
        else:
            print("Al menos uno de los equipos no es un país participante. Ingresa equipos válidos.")
    while True:
        try:
            puntos_local = int(input("Puntos del equipo local: "))
            puntos_visitante = int(input("Puntos del equipo visitante: "))
            break
        except ValueError:
            print("Ingresa valores numéricos válidos para los puntos")

    while True:
        fecha_str = input("Fecha del partido (formato DD/MM/AAAA): ")
        try:
            if len(fecha_str) == 5:
                fecha = datetime.strptime(fecha_str, "%d/%m")
            else:
                fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            fecha = fecha.replace(year=2023)
            break
        except ValueError:
            print("Ingresa una fecha válida en formato DD/MM/AAAA")

    zona = input("Zona: ").capitalize()

    partido = {
        "ID": nuevo_id,  # Asignar el nuevo ID automático
        "equipo_local": equipo_local,
        "equipo_visitante": equipo_visitante,
        "puntos_local": puntos_local,
        "puntos_visitante": puntos_visitante,
        "fecha": fecha.strftime("%d/%m/%Y"),
        "zona": zona,
    }

    return partido

# Función para modificar un partido
# Función para modificar un partido
def modificar_partido(partidos):
    print("Lista de partidos existentes:")
    for partido in partidos:
        print(f"ID: {partido['ID']}, Equipo Local: {partido['equipo_local']}, Equipo Visitante: {partido['equipo_visitante']}")

    partido_id = int(input("Ingrese el ID del partido que desea modificar: "))
    for partido in partidos:
        if int(partido["ID"]) == partido_id:
            equipo_local = input("Nuevo equipo local: ").capitalize()
            equipo_visitante = input("Nuevo equipo visitante: ").capitalize()
            puntos_local = int(input("Nuevos puntos del equipo local: "))
            puntos_visitante = int(input("Nuevos puntos del equipo visitante: "))
            fecha_str = input("Nueva fecha del partido (formato DD/MM/AAAA): ")
            try:
                fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            except ValueError:
                print("Ingresa una fecha válida en formato DD/MM/AAAA.")
                return
            zona = input("Nueva zona: ").capitalize()

            partido["equipo_local"] = equipo_local
            partido["equipo_visitante"] = equipo_visitante
            partido["puntos_local"] = puntos_local
            partido["puntos_visitante"] = puntos_visitante
            partido["fecha"] = fecha.strftime("%d/%m/%Y")
            partido["zona"] = zona

            print("El partido ha sido modificado exitosamente.")
            guardar_lista_partidos(partidos, nombre_archivo_csv, encabezados)  # Agregar esta línea
            return

    print("No se encontró un partido con el ID proporcionado.")

# Función para borrar un partido
def borrar_partido(partidos):
    print("Lista de partidos existentes:")
    for partido in partidos:
        print(f"ID: {partido['ID']}, Equipo Local: {partido['equipo_local']}, Equipo Visitante: {partido['equipo_visitante']}")

    partido_id = int(input("Ingrese el ID del partido que desea borrar: "))
    for partido in partidos:
        if int(partido["ID"]) == partido_id: 
            partidos.remove(partido)
            print(f"El partido con ID {partido_id} ha sido borrado exitosamente.")
            guardar_lista_partidos(partidos, nombre_archivo_csv, encabezados)  # Agregar esta línea
            return

    print("No se encontró un partido con el ID proporcionado.")

def guardar_partido(partido, nombre_archivo, encabezados):
    with open(nombre_archivo, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=encabezados)

        # Verifica si el archivo está vacío y escribe los encabezados si es necesario
        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(partido)

def mostrar_partidos(partidos):
    if not partidos:
        print("No hay datos cargados todavía...")
        return

    for partido in partidos:
        print("Datos del partido:")
        print(f"Partido ID: {partido['ID']}")
        print(f"Equipo local: {partido['equipo_local']}")
        print(f"Equipo visitante: {partido['equipo_visitante']}")
        print(f"Puntos del equipo local: {partido['puntos_local']}")
        print(f"Puntos del equipo visitante: {partido['puntos_visitante']}")
        print(f"Fecha: {partido['fecha']}")
        print(f"Zona: {partido['zona']}")
        print()

def mostrar_paises_puntajes(paises_participantes):
    for pais in paises_participantes:
        print(f"Pais: {pais['pais']}, Score: {pais['score']} puntos")

def cargar_partidos(nombre_archivo):
    partidos = []
    if not os.path.exists(nombre_archivo):
        return partidos

    with open(nombre_archivo, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            partidos.append(row)

    return partidos

def cargar_paises_participantes(nombre_archivo):
    paises_participantes = []
    with open(nombre_archivo, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            zona = row['zona']
            pais = row['pais']
            score = float(row['score'])
            paises_participantes.append({"zona": zona, "pais": pais, "score": score})
    return paises_participantes

def guardar_lista_partidos(partidos, nombre_archivo, encabezados):
    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=encabezados)
        writer.writeheader()
        for partido in partidos:
            writer.writerow(partido)

if __name__ == "__main__":
    nombre_archivo_csv = "./data/partidos.csv"
    encabezados = ["ID", "equipo_local", "equipo_visitante", "puntos_local",
                   "puntos_visitante", "fecha", "zona"]

    nombre_archivo_paises = "./data/paises.csv"
    paises_participantes = cargar_paises_participantes(nombre_archivo_paises)

    separador = "-" * 10

    while True:
        opcion = input(
            f"{separador} MENU {separador}\n1. Ingresar partido\n2. Mostrar partidos\n3. Mostrar "
            "todos los paises y scores\n4. Modificar partido\n5. Borrar partido\n6. Salir\nSeleccione una opcion: "
        )
        if opcion == "1":
            print(separador * 3)
            partido = ingresar_partido(paises_participantes)
            guardar_partido(partido, nombre_archivo_csv, encabezados)
        elif opcion == "2":
            print(separador * 3)
            partidos = cargar_partidos(nombre_archivo_csv)
            mostrar_partidos(partidos)
            if os.path.exists(nombre_archivo_csv):
                print("Puntajes de los equipos por zona:")
        elif opcion == "3":
            print(separador * 3)
            mostrar_paises_puntajes(paises_participantes)
        elif opcion == "4":
            print(separador * 3)
            partidos = cargar_partidos(nombre_archivo_csv)
            modificar_partido(partidos)
        elif opcion == "5":
            print(separador * 3)
            partidos = cargar_partidos(nombre_archivo_csv)
            borrar_partido(partidos)
        elif opcion == "6":
            print(separador * 3)
            print(separador * 3)
            break
        else:
            print("Opción no válida. Por favor ingrese una opción correcta.")
