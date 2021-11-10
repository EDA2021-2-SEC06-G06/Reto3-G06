"""
Reto 3 - view.py

Carlos Arturo Holguín Cárdenas
Daniel Hernández Pineda

 """

import config as cf
import sys
import controller
from datetime import datetime, date
from DISClib.ADT import list as lt
from DISClib.ADT import stack
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from time import process_time
from tabulate import tabulate
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


def printMenu():
    print("\n\n-----------------------------------------")
    print("Bienvenido al menú de opciones")
    print("-----------------------------------------")
    print("Opciones preliminares")
    print("1- Cargar datos")
    print("3- Consulta Lab 8")
    print("-----------------------------------------")
    print("Requerimientos")
    print("10- Consultar Requerimiento 1")
    print("20- Consultar Requerimiento 2")
    print("30- Consultar Requerimiento 3")
    print("40- Consultar Requerimiento 4")
    print("50- Consultar Requerimiento 5")
    print("-----------------------------------------")
    print("0- Salir\n")


def initCatalog():
    """
    Inicializa el catálogo
    """
    return controller.initCatalog()


def loadData(catalog, file_size):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadSightings(catalog, file_size)


def printFirst(lst, num):
    """
    Imprime los primeros num elementos de la lista
    """
    for pos in range(1,num+1):
        print(lt.getElement(lst, pos))
        print("")


def adjustlenght(text, step):
    """
    Inserta renglones en una cadena de caracteres para que se ajuste al formato de una tabla
    """
    lenght = len(text)

    for n in range(step, 20*step + 1, step):
        if lenght > n:
            text = text[:n] + "\n" + text[n:]
    
    return text


def printReq1Table(lst):
    """
    #Imprime la tabla del Requerimiento 1
    """
    headers = ["datetime", "city", "country", "shape", "duration (seconds)"]
    table = []
    size = lt.size(lst)

    for pos in range(1, size+1):
        sighting = lt.getElement(lst, pos)
        c1 = sighting["datetime"]
        c2 = sighting["city"]
        c3 = sighting["country"]
        c4 = sighting["shape"]
        c5 = sighting["duration (seconds)"]
        
        table.append([c1,c2,c3,c4,c5])

    print(tabulate(table, headers, tablefmt="grid"))


def printReq2Table(lstMin, lstMax):
    """
    Imprime la tabla del Requerimiento 2
    """
    headers = ['Date and Time','Country-City',"Duration (seconds)","Shape"]
    table = []

    if lt.size(lstMin)>=3:
        for pos in range(1,4):
            lista = lt.getElement(lstMin, pos)
            ListaF=lt.getElement(lista,1)
            c1 = adjustlenght(lt.getElement(ListaF,1), 25)
            c2 = adjustlenght(lt.getElement(ListaF,2), 18)
            c3 = adjustlenght(lt.getElement(ListaF,3), 15)
            c4 = adjustlenght(lt.getElement(ListaF,4), 15)
            

            table.append([c1,c2,c3,c4])
     

        for x in range(2, -1,-1):
            pos = lt.size(lstMax) - x
            lista = lt.getElement(lstMax, pos)
            ListaF=lt.getElement(lista,1)
            c1 = adjustlenght(lt.getElement(ListaF,1), 25)
            c2 = adjustlenght(lt.getElement(ListaF,2), 18)
            c3 = adjustlenght(lt.getElement(ListaF,3), 15)
            c4 = adjustlenght(lt.getElement(ListaF,4), 15)
        

            table.append([c1,c2,c3,c4])

    print(tabulate(table, headers, tablefmt="grid"))


def printReq3Table(lst_min, lst_max):
    """
    #Imprime la tabla del Requerimiento 3
    """
    headers = ["datetime", "city", "country", "shape", "duration (seconds)"]
    table=[]
    size = lt.size(lst_min) + lt.size(lst_max)

    if size>=3:
        for pos in range(1,4):
            sighting = lt.getElement(lst_min, pos)
            c1 = sighting["datetime"]
            c2 = sighting["city"]
            c3 = sighting["country"]
            c4 = sighting["shape"]
            c5 = sighting["duration (seconds)"]
            table.append([c1,c2,c3,c4,c5])
        
        for pos in range(1,4):
            sighting = lt.getElement(lst_max, pos)
            c1 = sighting["datetime"]
            c2 = sighting["city"]
            c3 = sighting["country"]
            c4 = sighting["shape"]
            c5 = sighting["duration (seconds)"]
            table.append([c1,c2,c3,c4,c5])


    else:
        for pos in range(1, lt.size(lst_min)+1):
            sighting = lt.getElement(lst_min, pos)
            c1 = sighting["datetime"]
            c2 = sighting["city"]
            c3 = sighting["country"]
            c4 = sighting["shape"]
            c5 = sighting["duration (seconds)"]
            table.append([c1,c2,c3,c4,c5])


    print(tabulate(table, headers, tablefmt="grid"))


def printReq4Table(lst):
    """
    Imprime la tabla del Requerimiento 4
    """
    headers = ["datetime", "city", "country", "shape", "duration (seconds)"]
    table = []

    #Primeros elementos
    for pos in range(1,4):
        sighting = lt.getElement(lst, pos)
        c1 = sighting["datetime"]
        c2 = sighting["city"]
        c3 = sighting["country"]
        c4 = sighting["shape"]
        c5 = sighting["duration (seconds)"]
        table.append([c1,c2,c3,c4,c5])

    #Últimos elementos
    for x in range(2, -1,-1):
        pos = lt.size(lst) - x
        sighting = lt.getElement(lst, pos)
        c1 = sighting["datetime"]
        c2 = sighting["city"]
        c3 = sighting["country"]
        c4 = sighting["shape"]
        c5 = sighting["duration (seconds)"]
        table.append([c1,c2,c3,c4,c5])

    print(tabulate(table, headers, tablefmt="grid"))


def printReq5Table(lst):
    """
    Imprime la tabla del Requerimientos 5
    """
    headers = ["datetime", "city", "country", "shape", "duration (seconds)", "latitude", "longitude"]
    table = []

    #Primeros elementos
    for pos in range(1,4):
        sighting = lt.getElement(lst, pos)
        c1 = sighting["datetime"]
        c2 = adjustlenght(sighting["city"], 20)
        c3 = sighting["country"]
        c4 = sighting["shape"]
        c5 = sighting["duration (seconds)"]
        c6 = sighting["latitude"]
        c7 = sighting["longitude"]
        table.append([c1,c2,c3,c4,c5,c6,c7])

    #Últimos elementos
    for x in range(2, -1,-1):
        pos = lt.size(lst) - x
        sighting = lt.getElement(lst, pos)
        c1 = sighting["datetime"]
        c2 = adjustlenght(sighting["city"], 20)
        c3 = sighting["country"]
        c4 = sighting["shape"]
        c5 = sighting["duration (seconds)"]
        c6 = sighting["latitude"]
        c7 = sighting["longitude"]
        table.append([c1,c2,c3,c4,c5,c6,c7])

    print(tabulate(table, headers, tablefmt="grid"))


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs) == 1:
        file_size = input("Ingrese el sufijo del archivo que desea utilizar (small, large, 10pct...): ")
        #file_size = "large"

        #Cargar archivos
        print("\nCargando información de los archivos ....")
        catalog = initCatalog()

        start_time = process_time()
        loadData(catalog, file_size)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000
        
        print("\nTiempo de carga: " + str(running_time) + " milisegundos")
        
        

    #Laboratorio 8
    elif int(inputs) == 3:
        height = om.height(catalog["MapLab8"])
        size = om.size(catalog["MapLab8"])

        print("\n\nLa altura es: " + str(height))
        print("El número de elementos (# de ciudades) es: " + str(size))



    #Requerimiento 1
    elif int(inputs) == 10:
        #city = input("\nIngrese el nombre de la ciudad a consultar: ")

        #Para pruebas
        city = "las vegas"

        start_time = process_time()
        req1, num_sightings = controller.REQ1(catalog, city)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000

        print("\n\n=============== Requerimiento Número 1 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " milisegundos")

        print("\nHubo " + str(num_sightings) + " avistamientos en la ciudad de '" + city + "'")
        printReq1Table(req1)
        
    
    
    #Requerimiento 2
    elif int(inputs) == 20:
        timeInitial = float(input("Por favor ingrese el limite inferior en segundos: "))
        timeFinal = float(input("Por favor ingrese el limite superior en segundos: "))
        start_time = process_time()
        NumberOfSightingsMax, ListMin, ListMax, TimeMax = controller.REQ2(catalog, timeInitial, timeFinal)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000
        
        print("\n\n=============== Requerimiento Número 2 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " milisegundos")
        print("\n Se registraron un total de "+str(NumberOfSightingsMax)+ " avistamientos con duracion de "+str(TimeMax)+" segundos")
        print("A continuacion se mostrar la informacion de los tres primeros y tres últimos avistamientos dentro del rango, ordenados cronológicamente")
        printReq2Table(ListMin, ListMax)
    

        
    #Requerimiento 3
    elif int(inputs) == 30:
        #time_low = input("Ingrese la hora inferior en formato HH:MM ")
        #time_high = input("Ingrese la hora superior en formato HH:MM ")

        #Para pruebas - peor caso
        time_low = "00:00"
        time_high = "23:59"

        start_time = process_time()
        req3_min, req3_max, num_sightings = controller.REQ3(catalog, time_low, time_high)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000

        print("\n\n=============== Requerimiento Número 3 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " milisegundos")

        print("\nHubo " + str(num_sightings) + " avistamientos entre las " + time_low + " y las " + time_high)
        printReq3Table(req3_min, req3_max)

    

    #Requerimiento 4
    elif int(inputs) == 40:
        #date_low = input("Ingrese la fecha inferior en formato AAAA-MM-DD: ")
        #date_high = input("Ingrese la fecha superior en formato AAAA-MM-DD: ")

        #Para pruebas - peor caso
        date_low = "1906-11-11"
        date_high = "2014-05-08"

        start_time = process_time()
        req4, num_sightings = controller.REQ4(catalog, date_low, date_high)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000

        print("\n\n=============== Requerimiento Número 4 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " milisegundos\n")

        print("Hubo " + str(num_sightings) + " avistamientos entre " + date_low + " y " + date_high)
        printReq4Table(req4)



    #Requerimiento 5
    elif int(inputs) == 50:
        #longitudeInitial = float(input("Por favor ingrese la longitud inicial con dos cifras decimales: "))
        #longitudeFinal = float(input("Por favor ingrese la longitud final con dos cifras decimales: "))
        #latitudeInitial = float(input("Por favor ingrese la latitud inicial con dos cifras decimales: "))
        #latitudeFinal = float(input("Por favor ingrese la latitud final con dos cifras decimales: "))
        
        #Para pruebas - peor caso
        longitudeInitial = -176.66
        longitudeFinal = 178.44
        latitudeInitial = -82.86
        latitudeFinal = 72.7

        start_time = process_time()
        NumberOfSightings,req5 = controller.REQ5(catalog, longitudeInitial, longitudeFinal,
                                                          latitudeInitial, latitudeFinal)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000

        print("\n\n=============== Requerimiento Número 5 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " milisegundos\n")
        print("Se encontraron "+str(NumberOfSightings)+ " avistamientos dentro del área definida")
        printReq5Table(req5)
        


    else:
        sys.exit(0)

sys.exit(0)
