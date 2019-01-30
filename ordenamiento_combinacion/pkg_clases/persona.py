#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria


class Persona(object):
    """Clase Persona: Guarda una referencia a una persona"""

    def __init__(self, nombre: str, apellido: str, edad: int):
        """Metodo constructor de la clase"""
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        """MEtodo que devuelve el objeto en formato de texto"""
        # {:n} n siendo un valor numerico para asignar un espaciado predefinido
        return '{:8} {:10} {:3}'.format(self.nombre, self.apellido, self.edad)
