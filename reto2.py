
diaActual = 31
anioActual = 2021
mesActual = 5
nombre = input("Ingrese su Nombre Completo: ")

while True:
    try:
        anioNacimiento = int(input("Año de Nacimiento: "))
        if anioNacimiento <= anioActual:
            break
    except TypeError:
        print("Tipo de dato no valido. Ingrese un número.")

while True:
    try:
        mesNacimiento = int(input("Mes de Nacimiento: "))
        if mesNacimiento > 0 and mesNacimiento <= 12:
            break
        else:
            print("Mes no Valido. Ingrese un numero del 1 al 12")
    except TypeError:
        print("Tipo de dato no valido. Ingrese un número.")

while True:
    try:
        diaNacimiento = int(input("Dia de Nacimiento: "))
        if mesNacimiento == 2:
            if anioNacimiento % 4 == 0:
                if anioNacimiento % 400 == 0:
                    maxDias = 29
                elif anioNacimiento % 100 == 0:
                    maxDias = 28
                else:
                    maxDias = 28
            else:
                maxDias = 28

        if mesNacimiento == 4 or mesNacimiento == 6 or mesNacimiento == 9 or mesNacimiento == 11:
            maxDias = 30
        else:
            maxDias = 31

        if diaNacimiento > 0 and diaNacimiento <= maxDias:
            break
        else:
            print("Dia no Valido")

    except TypeError:
        print("Tipo de dato no valido. Ingrese un número.")

while True:
    try:
        anioRegistro = int(input("Año de Registro: "))
        if anioNacimiento <= anioActual:
            break
    except TypeError:
        print("Tipo de dato no valido. Ingrese un número.")

while True:
    try:
        mesRegistro = int(input("Mes de Registro: "))
        if mesRegistro > 0 and mesRegistro <= 12:
            break
        else:
            print("Mes no Valido. Ingrese un numero del 1 al 12")
    except TypeError:
        print("Tipo de dato no valido. Ingrese un número.")

while True:
    try:
        diaRegistro = int(input("Dia de Registro: "))
        if mesRegistro == 2:
            if anioRegistro % 4 == 0:
                if anioRegistro % 400 == 0:
                    maxDias = 29
                elif anioRegistro % 100 == 0:
                    maxDias = 28
                else:
                    maxDias = 28
            else:
                maxDias = 28

        if mesRegistro == 4 or mesRegistro == 6 or mesRegistro == 9 or mesRegistro == 11:
            maxDias = 30
        else:
            maxDias = 31

        if diaRegistro > 0 and diaRegistro <= maxDias:
            break
        else:
            print("Dia no Valido")

    except TypeError:
        print("Tipo de dato no valido. Ingrese un número.")


anios = anioActual - anioNacimiento
meses = mesActual - mesNacimiento
edad = 0
if meses == 0:
    if (diaActual - diaNacimiento) >= 0:
        edad = anios
    else:
        edad = anios - 1
if meses > 0:
    edad = anios
if meses < 0:
    edad = anios - 1

if edad > 40:
    cumpleEdad = True
else:
    cumpleEdad = False

while(True):
    hipertencion = input("¿ Sufre usted de Hipertensión ?  Si/No: ")
    if hipertencion == "Si" or hipertencion == "SI" or hipertencion == "sI" or hipertencion == "si":
        hipertencion = True
        break
    if hipertencion == "No" or hipertencion == "NO" or hipertencion == "nO" or hipertencion == "NO":
        hipertencion = False
        break
    else:
        print("Respuesta NO valida, Responda Si o No")

while(True):
    epoc = input("¿ Sufre usted de EPOC ?  Si/No: ")
    if epoc == "Si" or epoc == "SI" or epoc == "sI" or epoc == "si":
        epoc = True
        break
    if epoc == "No" or epoc == "NO" or epoc == "nO" or epoc == "NO":
        epoc = False
        break
    else:
        print("Respuesta NO valida, Responda Si o No")

while(True):
    corazon = input("¿ Sufre usted del Corazón ?  Si/No: ")
    if corazon == "Si" or corazon == "SI" or corazon == "sI" or corazon == "si":
        corazon = True
        break
    if corazon == "No" or corazon == "NO" or corazon == "nO" or corazon == "NO":
        corazon = False
        break
    else:
        print("Respuesta NO valida, Responda Si o No")

if hipertencion or epoc or corazon or cumpleEdad:
    apto = "Si"
else:
    apto = "No"

razones = "\n"
if hipertencion:
    razones += "-Sufre de Hipertensión.\n"
else:
    razones += "-No sufre de Hipertensión.\n"
if epoc:
    razones += "-Sufre de EPOC.\n"
else:
    razones += "-No sufre de EPOC.\n"
if corazon:
    razones += "-Sufre del Corazon.\n"
else:
    razones += "-No sufre del Corazon.\n"
if cumpleEdad:
    razones += "-Es mayor de 40 años.\n"
else:
    razones += "-No es mayor de 40 años.\n"

# Salida
print("---------------------------------")
print()
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Apto para vacunarse: ", apto)
print("Porque: ", razones)
print()
