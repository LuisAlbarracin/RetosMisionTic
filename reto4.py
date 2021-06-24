# Programa de una Fecha de Futbol Reto 4

while True:
    try:
        cantidadPartidos = int(input("Ingrese la cantidad de partidos: "))
        if cantidadPartidos >= 5:
            break
        else:
            print("La cantidad de partidos debe ser mayor o igual a 5")
    except ValueError:
        print("Ingrese un número")

partidosFecha = []
clasificacionPuntos = []
i = 0
while i < cantidadPartidos:
    print("Partido: ", i + 1)
    while True:
        try:
            equipoLocal = input("Ingrese el nombre del equipo local: ")
            golesEquipoLocal = int(input("Ingrese la cantidad de goles del equipo local: "))
            break
        except ValueError:
            print("Ingrese un número en cantidad de goles")

    while True:
        try:
            equipoVisitante = input("Ingrese los el nombre del equipo visitante: ")
            golesEquipoVisitante = int(input("Ingrese la cantidad de goles del equipo visitante: "))
            break
        except ValueError:
            print("Ingrese un número en cantidad de goles")

    partido = [equipoLocal, golesEquipoLocal, equipoVisitante, golesEquipoVisitante]
    partidosFecha.append(partido)

    puntosLocal = 0
    puntosVisitante = 0

    if golesEquipoLocal == golesEquipoVisitante:
        puntosLocal = 1
        puntosVisitante = 1
    elif golesEquipoLocal > golesEquipoVisitante:
        puntosLocal = 3
        puntosVisitante = 0
    elif golesEquipoLocal < golesEquipoVisitante:
        puntosLocal = 0
        puntosVisitante = 3

    datosLocal = [equipoLocal, golesEquipoLocal, puntosLocal]
    datosVisitante = [equipoVisitante, golesEquipoVisitante, puntosVisitante]
    clasificacionPuntos.append(datosLocal)
    clasificacionPuntos.append(datosVisitante)
    i += 1



equipoConMasGoles = ""
equipoConMenosGoles = ""
masGoles = 0
menosGoles = 100
cantidadGoles = 0
print("--- Partidos de la Jornada ---")
for i in range(len(partidosFecha)):
    print(partidosFecha[i][0], " ", partidosFecha[i][1], " - ", partidosFecha[i][3], " ", partidosFecha[i][2])
    cantidadGoles += partidosFecha[i][1]
    cantidadGoles += partidosFecha[i][3]
    if partidosFecha[i][1] > masGoles:
        masGoles = partidosFecha[i][1]
        equipoConMasGoles = partidosFecha[i][0]
    if partidosFecha[i][3] > masGoles:
        masGoles = partidosFecha[i][3]
        equipoConMasGoles = partidosFecha[i][2]

    if partidosFecha[i][1] < menosGoles:
        menosGoles = partidosFecha[i][1]
        equipoConMenosGoles = partidosFecha[i][0]
    if partidosFecha[i][3] < menosGoles:
        menosGoles = partidosFecha[i][3]
        equipoConMenosGoles = partidosFecha[i][2]

promedio = cantidadGoles / cantidadPartidos

print("\n Tabla de posiciones")
print("\n Equipo    Goles     Puntos")
for i in range(len(clasificacionPuntos)):
    print(clasificacionPuntos[i][0], " ", clasificacionPuntos[i][1], " ", clasificacionPuntos[i][2])

print("\n")
print("--- Estadisticas ---")
print("Cantidad de Goles: ", cantidadGoles)
print("Promedio de Goles: ", promedio)
print("Equipo con mas goles anotados: ", equipoConMasGoles, " : ", masGoles)
print("Equipo con menos goles anotados: ", equipoConMenosGoles, " : ", menosGoles)
