#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

import codecs
import sys


class MiArchivo(object):

    # Constructor de clase
    def __init__(self, nombre):
        self.archivo = codecs.open('data/{}'.format(nombre), 'r')

    # Metodo que devuelve todas las lineas del archivo
    def obtener_informacion(self):
        return self.archivo.readlines()

    # Metodo que cierra la lectura del archivo
    def cerrar_archivo(self):
        self.archivo.close()
