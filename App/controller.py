"""
Reto 3 - controller.py

Carlos Arturo Holguín Cárdenas
Daniel Hernández Pineda

 """

import config as cf
import model
import csv


# ==============================================
# Inicialización del catálogo de obras
# ==============================================

def initCatalog():
    """
    Llama la funcion de inicializació del catálogo del modelo
    """
    catalog = model.newCatalog()
    return catalog



# ==============================================
# Funciones para la carga de datos
# ==============================================
def loadSightings(catalog, file_size):
    """
    Carga los artistas del archivo
    """
    artistsfile = cf.data_dir + 'UFOS-utf8-' + file_size + '.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for sighting in input_file:
        model.AddCitiesREQ1(catalog, sighting)
        model.AddTimesREQ3(catalog, sighting)
        model.AddDatesREQ4(catalog, sighting)
        model.AddDurationTreeREQ2(catalog, sighting)
        model.AddLongitudesREQ5(catalog, sighting)
        model.AddCitiesLab8(catalog, sighting)
    model.AddDatesListsREQ3(catalog["MapReq3"]["root"])


# ==============================================
# Funciones de consulta sobre el catalogo
# ============================================

#Requerimiento 1
def REQ1(catalog, city):
    return model.REQ1(catalog, city)

#Requerimiento 2
def REQ2(catalog, timeInitial, timeFinal):
    return model.REQ2(catalog, timeInitial, timeFinal)

#Requerimiento 3
def REQ3(catalog, time_low, time_high):
    return model.REQ3(catalog, time_low, time_high)

#Requerimiento 4
def REQ4(catalog, date_low, date_high):
    return model.REQ4(catalog, date_low, date_high)

#Requerimiento 5
def REQ5(catalog, longitudeInitial, LongitudeFinal, LatitudeInitial, LatitudeFinal):
    return model.REQ5(catalog, longitudeInitial, LongitudeFinal, LatitudeInitial, LatitudeFinal)