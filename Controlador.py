from Perro import Perro
from Vista import Vista



class Controlador:
    def __init__(self):
        self.Perro = Perro(nombre='',edad='',color='',raza='',sexo='',tamaño='')
        self.Vista = Vista()
        self.listaperros = []


    def cargar_archivo(self):
        with open("perros.txt","r",encoding="utf-8") as file:
            for linea in file.readlines():
                linea = linea.strip().split(",")
                self.Perro = Perro(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5])
                self.listaperros.append(self.Perro)

    def guardar_archivo(self):
        with open("perros.txt","a",encoding="utf-8")as file:
                file.write(str(self.Perro.get_nombre())+","+(str(self.Perro.get_edad()))+","+(str(self.Perro.get_color()))+","+(str(self.Perro.get_raza()))+","+(str(self.Perro.get_sexo()))+","+(str(self.Perro.get_tamaño()))+'\n')

    def crear_archivo(self):
            with open("perros.txt","a+") as archivo:
                archivo.seek(0)
                contenido = archivo.read()
                if len(contenido) == 0:
                    archivo.write(str(self.Perro.get_nombre())+","+(str(self.Perro.get_edad()))+","+(str(self.Perro.get_color()))+","+(str(self.Perro.get_raza()))+","+(str(self.Perro.get_sexo()))+","+(str(self.Perro.get_tamaño()))+'\n')


    def ejecutar_menu(self):
        self.crear_archivo()
        opcion = 0
        while opcion != "5":
            try:
                opcion = self.Vista.menu()
                if opcion == "1":
                    self.ingresar_datos_perro()
                if opcion == "2":
                    self.consultar_datos_perro()
                if opcion == "3":
                    self.eliminar_perro()
                if opcion == "4":
                    self.mostrar_lista_perros()
            except ValueError:
                self.Vista.manejo_de_errores()
                self.ejecutar_menu()
        self.Vista.gracias_por_utilizar_nuestro_programa()

    def ingresar_datos_perro(self):
        nombre = self.Vista.pedir_nombre_perro()
        edad = self.Vista.pedir_edad_perro()
        color = self.Vista.pedir_color_perro()
        raza = self.Vista.pedir_raza_perro()
        sexo = self.Vista.pedir_sexo_perro()
        tamaño = self.Vista.pedir_tamaño_perro()
        self.Perro.set_nombre(nombre)
        self.Perro.set_edad(edad)
        self.Perro.set_color(color)
        self.Perro.set_raza(raza)
        self.Perro.set_sexo(sexo)
        self.Perro.set_tamaño(tamaño)
        Perro(nombre,edad,color,raza,sexo,tamaño)
        self.guardar_archivo()
        self.cargar_archivo()
        aux = self.Vista.consultar_si_desea_ingresar_otro_perro()
        if aux == "S":
            self.ingresar_datos_perro()
        if aux == "N":
            self.ejecutar_menu()



    def mostrar_lista_perros(self):
        with open("perros.txt","r") as file:
            for linea in file:
                datos = linea.strip().split(",")
                listaperros = datos[]
                

                
  
            

    def consultar_datos_perro(self):
        encontrado = False
        nombre_perro = self.Vista.pedir_nombre_perro()
        with open("perros.txt","r") as file:
            for linea in file:
                datos = linea.strip().split(",")
                nombre = datos[0]
                if nombre == nombre_perro:
                    edad = datos[1]
                    color = datos[2]
                    raza = datos[3]
                    sexo = datos[4]
                    tamaño = datos[5]
                    return self.Vista.mostrar_datos_perro(nombre,edad,color,raza,sexo,tamaño)
            self.ejecutar_menu()
        return None



