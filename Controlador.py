from Perro import Perro
from Vista import Vista



class Controlador:
    def __init__(self):
        self.Perro = Perro(nombre='',edad='',color='',raza='',sexo='',tamaño='')
        self.Vista = Vista
        self.listaperros = []


    def cargar_archivo(self):
        with open("archivo.txt","r") as file:
            for linea in file.readlines():
                linea = linea.strip().split(";")
                perro = Perro(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5])
                self.listaperros.append(perro)

    def guardar_archivo(self,perro):
        with open("archivo.txt","w",encoding="utf-8")as file:
            for perro in self.listaperros:
                perros = []



    def ejecutar_menu(self):
        opcion = self.Vista.menu()
        if opcion == 1:
            self.ingresar_datos_perro()
        if opcion == 2:
            self.consultar_datos_perro()
        if opcion == 3:
            self.eliminar_perro()


    def ingresar_datos_perro(self):
        nombre = self.Vista.pedir_nombre_perro()
        edad = self.Vista.pedir_edad_perro()
        color = self.Vista.pedir_color_perro()
        raza = self.Vista.pedir_raza_perro()
        sexo = self.Vista.pedir_sexo_perro()
        tamaño = self.Vista.pedir_tamaño_perro()
        Perro(nombre,edad,color,raza,sexo,tamaño)
        self.cargar_archivo()

    def consultar_datos_perro(self):
        with open