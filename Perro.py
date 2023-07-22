from typing import Any


class Perro:
    def __init__(self,nombre,edad,color,raza,sexo,tamaño):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.raza = raza
        self.sexo = sexo
        self.tamaño = tamaño


    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_color(self):
        return self.color
    def get_raza(self):
        return self.raza
    def get_sexo(self):
        return self.sexo
    def get_tamaño(self):
        return self.tamaño
    

    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_edad(self,edad):
        self.edad = edad
    def set_color(self,color):
        self.color = color
    def set_raza(self,raza):
        self.raza = raza
    def set_sexo(self,sexo):
        self.sexo = sexo
    def set_tamaño(self,tamaño):
        self.tamaño = tamaño

def __str__(self):
    return("El nombre del perro es"+str(self.nombre)+"su edad es de "+str(self.edad)+"su color es "+str(self.color)+"Su raza es"+str(self.raza)+"su sexo es"+str(self.sexo)+"Su tamaño es "+str(self.tamaño))

