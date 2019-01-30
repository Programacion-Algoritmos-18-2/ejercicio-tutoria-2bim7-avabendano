#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

from pkg_orden.combinacion import merge_sort
from pkg_archivos.miarchivo import MiArchivo
from pkg_clases.persona import Persona

# Creamos un objeto que lea los datos del CSV
archivoDatos = MiArchivo('data.csv')
# Obtenemos todas las lineas del documento
datosStr = archivoDatos.obtener_informacion()

# Creamos una lista vacia
personas = []

# Recorremos cada linea
for linea in datosStr:
    # Remplazamos los saltos de linea con vacio y separamos los valores por ;
    datos = linea.replace('\n', '').split(';')
    # Creamos y añadimos una nueva Persona a la lista
    personas.append(Persona(datos[0], datos[1], int(datos[2])))

# Usamos el metodo merge_sort para ordenar nuestra lista
personasOrde = merge_sort(personas)

# Imprimimos el resultado ordenado
print()
for persona in personasOrde:
    print(persona)
print()