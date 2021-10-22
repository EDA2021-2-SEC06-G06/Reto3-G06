﻿"""
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

def loadData(catalog, file_size):
    """
    Carga los datos de los archivos
    """
    loadSightings(catalog, file_size)



def loadSightings(catalog, file_size):
    """
    Carga los artistas del archivo
    """
    artistsfile = cf.data_dir + 'UFOS-utf8-' + file_size + '.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for sighting in input_file:
        pass



# ==============================================
# Funciones de consulta sobre el catalogo
# ============================================

#Requerimiento 1
def REQ1(catalog):
    return model.REQ1(catalog)

#Requerimiento 2
def REQ2(catalog):
    return model.REQ2(catalog)

#Requerimiento 3
def REQ3(catalog,Name):
    return model.REQ3(catalog)

#Requerimiento 4
def REQ4(catalog):
    return model.REQ4(catalog)

#Requerimiento 5
def REQ5(catalog):
    return model.REQ5(catalog)