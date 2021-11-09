"""
Reto 3 - model.py

Carlos Arturo Holguín Cárdenas
Daniel Hernández Pineda

 """


import config as cf
from datetime import datetime
from DISClib.ADT import stack
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.Algorithms.Trees import traversal as re
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as mso
assert cf

# ==============================================
# Construccion de modelos
# ==============================================
def newCatalog():
    """
    Inicializa el catálogo de avistamientos
    """
    catalog = {"MapReq1": None,      
               "MapReq3": None,
               "MapReq4": None,        #Estructura principal es un hashmap
               "MapReq2.1": None,
               "MapReq5": None}      

    catalog["MapReq1"] = mp.newMap(1000,
                                     maptype='PROBING',
                                     loadfactor=0.5)

    catalog["MapReq3"] = om.newMap(omaptype="RBT")
    
    catalog["MapReq4"] = om.newMap(omaptype="RBT")
    catalog["MapReq2.1"] = om.newMap(omaptype="RBT")
    catalog["MapReq5"] = om.newMap(omaptype="RBT")
   
    
    return catalog



# ==============================================
# Funciones para agregar informacion al catalogo
# ============================================
def AddCitiesREQ1(catalog, sighting):
    """
    Crea una tabla de hash de la forma 'key'= city , 'value'= árbol de avistamientos ordenados por datetime
    """
    CitiesMap = catalog["MapReq1"]
    sighting_data = sightingData(sighting)
    city = sighting["city"]
    exists_city= mp.contains(CitiesMap, city)
    
    if not exists_city:    #Se crea la llave y el árbol de avistamientos
        city_info = om.newMap()
        om.put(city_info, sighting_data["datetime"], sighting_data)
        mp.put(CitiesMap, city, city_info)
    
    else:                  #Se añade el avistamiento en la ciudad ya existente 
        entry = mp.get(CitiesMap, city)
        city_info = me.getValue(entry)
        om.put(city_info, sighting_data["datetime"], sighting_data)


def AddTimesREQ3(catalog, sighting):
    """
    Crea un árbol cuyos nodos son de la forma 'key'= HH:MM, 'value'= lista de avistamientos
    """
    SightingsTree = catalog["MapReq3"]
    sighting_data = sightingData(sighting)
    time = datetime.strftime(sighting_data["datetime"], "%H:%M")
    entry = om.get(SightingsTree, time)
    
    if entry is None:           #Se crea la llave y la lista de avistamientos
        time_info = om.newMap()
        om.put(time_info, sighting_data["datetime"], sighting_data)
        om.put(SightingsTree, time, time_info)

    else:                       #Se añade el avistamiento en la hora:minuto ya existente 
        time_info = me.getValue(entry)
        om.put(time_info, sighting_data["datetime"], sighting_data)


def AddDatesREQ4(catalog, sighting):
    """
    Crea un árbol cuyos nodos son de la forma 'key'= fecha, 'value'= lista de avistamientos
    """
    SightingsTree = catalog["MapReq4"]
    sighting_data = sightingData(sighting)
    date = datetime.strftime(sighting_data["datetime"], "%Y-%m-%d")
    entry = om.get(SightingsTree, date)

    if entry is None:           #Se crea la llave y la lista de avistamientos
        date_info = lt.newList()
        lt.addLast(date_info, sighting_data)
        om.put(SightingsTree, date, date_info)

    else:                       #Se añade el avistamiento en la fecha ya existente 
        date_info = me.getValue(entry)
        lt.addLast(date_info, sighting_data)


def AddDurationTreeREQ2(catalog, sighting):
    """
    Se crea un árbol cuyos nodos son de la forma 'key'= duration , 'value'= arbol con key= Country-City, value= informacion necesaria en lista de listas
    """
    DurationTree = catalog["MapReq2.1"]
    duration = float(sighting["duration (seconds)"])
    EntryDuration=om.get(DurationTree,duration)
    Country = sighting["country"]
    City = sighting["city"]
    Country_City = Country+"-"+City
    if EntryDuration is None:                            #Se crea la llave y el árbol de Country...
        CountryCityInfo=om.newMap(omaptype="RBT")
        ListOfData = lt.newList("ARRAY_LIST")
        ListDataNecessary=DataNecessaryREQ2(sighting, Country_City)
        lt.addLast(ListOfData, ListDataNecessary)
        om.put(CountryCityInfo, Country_City, ListOfData)
        om.put(DurationTree, duration, CountryCityInfo)
    else:                                                   #Si ya esta el key de duracion
        DurationInfo=me.getValue(EntryDuration) 
        EntryCountry_City=om.get(DurationInfo, Country_City)
        if EntryCountry_City is None:                        #Se crea una nueva key dentro del subarbol 
            ListOfData = lt.newList("ARRAY_LIST")
            ListDataNecessary=DataNecessaryREQ2(sighting, Country_City)
            lt.addLast(ListOfData, ListDataNecessary)
            om.put(DurationInfo, Country_City, ListOfData)
        else:
            CountryInfo=me.getValue(EntryCountry_City)                 # Ya esta la key Country-City, entonces se agrega informacion a esa key del subarbol
            DataInThisCase=DataNecessaryREQ2(sighting, Country_City)
            lt.addLast(CountryInfo, DataInThisCase)
       

def AddLongitudesREQ5(catalog, sighting):
    """
    Crea un árbol cuyos nodos son de la forma 'key'= longitud, 'value'= árbol de avistamientos según latitud
    """
    LongitudeTree = catalog["MapReq5"]
    longitude = round(float(sighting["longitude"]),2)
    latitude = round(float(sighting["latitude"]),2)

    sighting_data = sightingData(sighting)
    longitude_entry = om.get(LongitudeTree, longitude)

    if longitude_entry is None:
        LatitudeTree = om.newMap(omaptype="RBT")
        sightings_list = lt.newList("ARRAY_LIST")
        lt.addLast(sightings_list, sighting_data)
        om.put(LatitudeTree, latitude, sightings_list)
        om.put(LongitudeTree, longitude, LatitudeTree)

    else:
        LatitudeTree= me.getValue(longitude_entry)
        latitude_entry = om.get(LatitudeTree, latitude)

        if latitude_entry is None:
            sightings_list = lt.newList("ARRAY_LIST")
            lt.addLast(sightings_list, sighting_data)
            om.put(LatitudeTree, latitude, sightings_list)

        else:
            sightings_list = me.getValue(latitude_entry)
            lt.addLast(sightings_list, sighting_data)



# ==============================================
# Funciones para creacion de datos
# ==============================================
def sightingData(sighting):
    "Filtra la información relevante para el primer requerimiento"
    date_time = sighting["datetime"]
    date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')

    sighting_data = {"datetime": date_time,
                     "city": sighting["city"],
                     "country": sighting["country"],
                     "shape": sighting["shape"],
                     "duration (seconds)": sighting["duration (seconds)"],
                     "longitude": round(float(sighting["longitude"]),2),
                     "latitude": round(float(sighting["latitude"]),2)}

    return sighting_data


def DataNecessaryREQ2(sighting, Country_City):
    ListFinalREQ2 = lt.newList("ARRAY_LIST")
    lt.addLast(ListFinalREQ2, sighting["datetime"])
    lt.addLast(ListFinalREQ2, Country_City)
    lt.addLast(ListFinalREQ2, sighting["duration (seconds)"])
    lt.addLast(ListFinalREQ2, sighting["shape"])
    return ListFinalREQ2



# ==============================================
# Funciones de consulta
# ==============================================

#Requerimiento 1
def addFirstREQ1(tree, lst, x):
    """
    Añade los primeros "x" elementos de un árbol a una lista
    Importante: "x" debe ser mayor que 1
    """
    tree_size = om.size(tree)
    key_low = om.minKey(tree)

    if tree_size >= x:  #Para asegurarse de no generar errores con ciudades de pocos avistamientos
        key_high = om.select(tree, (x - 1))
    else:
        key_high = om.maxKey(tree)

    elements = om.values(tree, key_low, key_high)
    elements_size = lt.size(elements)

    #Se añaden los elementos de la lista "elements" a la lista "lst"
    pos = 1
    while pos <= elements_size: #O(1) porque elements_size es siempre igual a "x", y el máximo "x" requerido es 5
        sighting = lt.getElement(elements, pos) #O(1) porque "elements" es un ARRAY_LIST (modificación en rbt.py)
        lt.addLast(lst, sighting)
        pos += 1


def addLastREQ1(tree, lst, x):
    """
    Añade los últimos "x" elementos de un árbol a una lista
    Importante: "x" debe ser mayor que 1
    """
    tree_size = om.size(tree)

    if tree_size >= 2*x:  #Para asegurarse de no generar errores con ciudades de pocos avistamientos
        key_low = om.select(tree, (tree_size - x))
        key_high = om.maxKey(tree)

    elif tree_size>x and tree_size<2*x:
        key_low = om.select(tree, x)
        key_high = om.maxKey(tree) 

    if tree_size>x:     #Para asegurarse de no repetir los elementos añadidos en addFirst()
        elements = om.values(tree, key_low, key_high)
        elements_size = lt.size(elements)

        #Se añaden los elementos de la lista "elements" a la lista "lst"
        pos = 1
        while pos <= elements_size: #O(1) porque elements_size es siempre igual a "x", y el máximo "x" requerido es 5
            sighting = lt.getElement(elements, pos) #O(1) porque "elements" es un ARRAY_LIST (modificación en rbt.py)
            lt.addLast(lst, sighting)
            pos += 1
    

def REQ1(catalog, city):
    """
    Crea una lista con los primeros y últimos 3 avistamientos de una ciudad dada organizados según fecha
    """
    CitiesMap = catalog["MapReq1"]
    city_entry = mp.get(CitiesMap, city)
    sightings_tree = me.getValue(city_entry)

    first_last_elem = lt.newList("ARRAYLIST")
    num_sightings = om.size(sightings_tree)

    addFirstREQ1(sightings_tree, first_last_elem, 3)
    addLastREQ1(sightings_tree, first_last_elem, 3)

    return first_last_elem, num_sightings


#Requerimiento 2
def REQ2(catalog, timeInitial, timeFinal):
    i=1
    k=1
    TreeOfDuration = catalog["MapReq2.1"]
    TreeFinalMin = om.newMap(omaptype="RBT")
    TreeFinalMax = om.newMap(omaptype="RBT")
    FloorDurationmax = om.floor(TreeOfDuration, timeFinal)            #Se halla rango minimo
    FloorDurationMin = om.floor(TreeOfDuration,timeInitial)           #Se halla rango maximo
    Entrymax = om.get(TreeOfDuration, FloorDurationmax)
    ValueMaxDuration = me.getValue(Entrymax)
    Entrymin = om.get(TreeOfDuration, FloorDurationMin)               #Se piden valores
    ValueMinDuration = me.getValue(Entrymin)
    NumberOfSightingsMax = om.size(ValueMaxDuration)
    #Obtener lista con datos minimos y maximos
    DataMin = re.inorder(ValueMinDuration)                         #Se recorre en orden
    DataMax = re.inorder(ValueMaxDuration)
    while i<=lt.size(DataMin):
        Data= lt.getElement(DataMin, i)
        ListWithData = lt.newList("ARRAY_LIST")
        SubList = lt.getElement(Data, 1)
        lt.addLast(ListWithData, lt.getElement(SubList, 1))
        lt.addLast(ListWithData, lt.getElement(SubList, 2))
        lt.addLast(ListWithData, lt.getElement(SubList, 3))
        lt.addLast(ListWithData, lt.getElement(SubList, 4))
        om.put(TreeFinalMin, lt.getElement(SubList, 1), ListWithData)
        i+=1
    while k<=lt.size(DataMax):
        Data= lt.getElement(DataMax, k)
        SubList = lt.getElement(Data, 1)
        ListWithData = lt.newList("ARRAY_LIST")
        lt.addLast(ListWithData, lt.getElement(SubList, 1))
        lt.addLast(ListWithData, lt.getElement(SubList, 2))
        lt.addLast(ListWithData, lt.getElement(SubList, 3))
        lt.addLast(ListWithData, lt.getElement(SubList, 4))
        om.put(TreeFinalMax, lt.getElement(SubList, 1), ListWithData)
        k+=1
    DataMinF = re.inorder(TreeFinalMin)                         #Se recorre en orden
    DataMaxF = re.inorder(TreeFinalMax)

    return NumberOfSightingsMax, DataMinF, DataMaxF, FloorDurationmax


#Requerimiento 3
def REQ3(catalog, time_low, time_high):
    """
    Devuelve una lista con los avistamientos entre una hora time_low y una hora time_high
    """
    SightingsTree = catalog["MapReq3"]
    sightings = om.values(SightingsTree, time_low, time_high) #Corresponde a una lista de árboles
    #final_list = lt.newList("ARRAY_LIST")
    final_tree = om.newMap()
    
    sightings_size = lt.size(sightings)
    pos = 1

    while pos <= sightings_size: #El máximo de ciclos realizados es num_parejas_hora_minuto
        subtree = lt.getElement(sightings, pos)
        sublist = om.valueSet(subtree)
        sublist_size = lt.size(sublist)
        i = 1

        while i <= sublist_size: #El número de ciclos depende del número de avistamientos en la misma hora:minuto
            sighting = lt.getElement(sublist, i)
            #lt.addLast(final_list, sighting)
            om.put(final_tree, sighting["datetime"], sighting)
            i += 1

        pos += 1

    num_sightings = om.size(final_tree)   #lt.size(final_list)
    min_list, max_list = processInfoREQ3(final_tree, )

    return min_list, max_list, num_sightings


def processInfoREQ3(info_tree):
    """
    Filtra los primeros y últimos 3 avistamientos en el rango y los retorna en una lista
    """

    size = om.size(info_tree)

    min = om.minKey(info_tree)
    min_3 = om.select(info_tree, 2)
    max = om.maxKey(info_tree)
    max_3 = om.select(info_tree, size-3)

    min_list = om.values(info_tree, min, min_3)
    max_list = om.values(info_tree, max_3, max)

    return min_list, max_list


#Requerimiento 4
def REQ4(catalog, date_low, date_high):
    """
    Devuelve una lista con los avistamientos entre una fecha date_low y una fecha date_high
    """
    SightingsTree = catalog["MapReq4"]
    sightings = om.values(SightingsTree, date_low, date_high) #Corresponde a una lista de listas
    final_list = lt.newList("ARRAY_LIST")

    sightings_size = lt.size(sightings)
    pos = 1

    while pos <= sightings_size: #El máximo de ciclos realizados es num_fechas
        sublist = lt.getElement(sightings, pos)
        sublist_size = lt.size(sublist)
        i = 1

        while i <= sublist_size: #El número de ciclos depende del número de avistamientos en la misma fecha
            sighting = lt.getElement(sublist, i)
            lt.addLast(final_list, sighting)
            i += 1

        pos += 1

    num_sightings = lt.size(final_list)

    return final_list, num_sightings


#Requerimiento 5
def REQ5(catalog, longitudeInitial, longitudeFinal, latitudeInitial, latitudeFinal):

    LongitudeTree = catalog["MapReq5"]
    longitudesInRange = om.values(LongitudeTree, longitudeInitial, longitudeFinal)
    
    longitudes_size = lt.size(longitudesInRange)
    ListFinal = lt.newList("ARRAY_LIST")
    pos_longitude = 1

    while pos_longitude <= longitudes_size:
        LatitudeTree = lt.getElement(longitudesInRange, pos_longitude)
        latitudesInRange = om.values(LatitudeTree, latitudeInitial, latitudeFinal)
        latitudes_size = lt.size(latitudesInRange)
        pos_latitude = 1

        while pos_latitude <= latitudes_size:
            sublist = lt.getElement(latitudesInRange, pos_latitude)
            sublist_size = lt.size(sublist)
            i = 1

            while i <= sublist_size:
                sighting = lt.getElement(sublist, i)
                lt.addLast(ListFinal, sighting)
                
                i += 1

            pos_latitude += 1

        pos_longitude+=1
            

    NumberOfSightings = lt.size(ListFinal)

    return NumberOfSightings, ListFinal

