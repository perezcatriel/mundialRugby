import csv


def ingresar_partido(paises_participantes):
    while True:
        equipo_local = input("Equipo local: ")
        equipo_visitante = input("Equipo visitante: ")

        if any(
                pais["pais"] == equipo_local for pais in paises_participantes
                ) and any(
                pais["pais"] == equipo_visitante for pais in
                paises_participantes
                ):
            break
        else:
            print("Al menos uno de los equipos no es un país participante. Ingresa equipos válidos.")

    puntos_local = input("Puntos del equipo local: ")
    puntos_visitante = input("Puntos del equipo visitante: ")
    fecha = input("Fecha del partido: ")
    zona = input("Zona: ")

    partido = {
        "equipo_local": equipo_local,
        "equipo_visitante": equipo_visitante,
        "puntos_local": puntos_local,
        "puntos_visitante": puntos_visitante,
        "fecha": fecha,
        "zona": zona,
    }

    return partido


def guardar_partido(partido, nombre_archivo, encabezados):
    with open(nombre_archivo, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=encabezados)

        # Verifica si el archivo está vacío y escribe los encabezados si es necesario
        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(partido)


def mostrar_partidos(nombre_archivo):
    with open(nombre_archivo, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            print("Datos del partido:")
            print(f"Equipo local: {row['equipo_local']}")
            print(f"Equipo visitante: {row['equipo_visitante']}")
            print(f"Puntos del equipo local: {row['puntos_local']}")
            print(f"Puntos del equipo visitante: {row['puntos_visitante']}")
            print(f"Fecha: {row['fecha']}")
            print(f"Zona: {row['zona']}")
            print()

def mostrar_paises_puntajes(paises_participantes):
    for pais in paises_participantes:
        print(f"Pais: {pais['pais']}, Score: {pais['score']} puntos")


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



if __name__ == "__main__":
    nombre_archivo_csv = "./data/partidos.csv"
    encabezados = ["equipo_local", "equipo_visitante", "puntos_local",
                   "puntos_visitante", "fecha", "zona"]

    nombre_archivo_paises = "./data/paises.csv"
    paises_participantes = cargar_paises_participantes(nombre_archivo_paises)

    while True:
        opcion = input(
                "1. Ingresar partido\n2. Mostrar partidos\n3. Mostrar "
                "todos los paises y scores\n4. "
                "Salir\nSeleccione una opcion: "
                )
        if opcion == "1":
            partido = ingresar_partido(paises_participantes)
            guardar_partido(partido, nombre_archivo_csv, encabezados)
        elif opcion == "2":
            mostrar_partidos(nombre_archivo_csv)
            print("Puntajes de los equipos por zona:")
        elif opcion == "3":
            mostrar_paises_puntajes(paises_participantes)
        elif opcion == "4":
            break
        else:
            print("Opcion no valido. Por favor ingrese una opcion correcta.")
