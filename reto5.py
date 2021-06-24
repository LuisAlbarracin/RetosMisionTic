# Reto 5
# Eventos de dengue ocurridos en el año 2015


try:
    archivo = open("archivo/eventos_2015.txt")
    contador = 0
    lista_eventos = []
    for linea in archivo:
        if contador > 0:
            linea = linea.replace("\n", "")
            linea_datos = linea.split(";")
            linea_datos[2] = int(linea_datos[2])
            lista_eventos.append(linea_datos)
        contador += 1

except FileNotFoundError:
    print("Archivo no encontrado")
else:
    print("Archivo encontrado")

cantidadHombreHospitalizados = 0
mujeresBarrioLaCumbre = 0
registroMenores = 0
mesJulio = 0

for datos in lista_eventos:
    if datos[3] == 'M' and datos[6] == 'Si':
        cantidadHombreHospitalizados += 1
    if datos[3] == 'F' and datos[4] == 'LA CUMBRE':
        mujeresBarrioLaCumbre += 1
    if datos[2] <= 18:
        registroMenores += 1
    sub_linea_fecha = datos[1].split("-")
    anio = sub_linea_fecha[0]
    mes = sub_linea_fecha[1]
    dia = sub_linea_fecha[2]
    if (mes == '07'):
        mesJulio += 1


def porEdadMenorMujeres(registro):
    return [registro[3], registro[2]]


print()
print("Registro de Mujeres de Menor Edad")
print("FECHA ------- BARRIO-------EDAD")
lista_eventos.sort(key=porEdadMenorMujeres, reverse=False)

for i in range(0, 5, 1):
    print(lista_eventos[i][0],lista_eventos[i][1], " - ", lista_eventos[i][4], " - ", lista_eventos[i][2])


def porEdadMayor(registro):
    return [registro[2]]


lista_eventos.sort(key=porEdadMayor, reverse=True)
print()
print("20 Registros con mayor edad")
print("FECHA ------- BARRIO-------EDAD")
for i in range(0, 20, 1):
    print(lista_eventos[i][1], " - ", lista_eventos[i][4], " - ", lista_eventos[i][2])

print()
print("Cantidad de hombres hospitalizados: ", cantidadHombreHospitalizados)
print("Cantidad de Mujeres que viven en el Barrio la cumbre: ", mujeresBarrioLaCumbre)
print("Registros de igual o menor a 18 años de edad: ", registroMenores)
print("Registros en el mes de Julio: ", mesJulio)
