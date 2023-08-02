import time
import os

class Vista:
    def __init__(self):
        pass



    def menu(self):
        print("----------------------------------")
        print("             PERRO                ")
        print("[1] Ingresar Perro nuevo")
        print("[2] Consultar Datos de Perro")
        print("[3] Eliminar Perro de La BD")
        print("[4] Mostrar Lista Perros")
        print("[5] Salir Del Programa")
        print("----------------------------------")
        return input("Ingrese una opcion valida por favor\n->")

    def pedir_nombre_perro(self):
        return input("Ingrese el nombre de su Perro:\n->")
    
    def pedir_edad_perro(self):
        return input("Ingrese la edad de su Perro\n->")

    def pedir_color_perro(self):
        return input("Ingrese el color de su Perro\n->")
    
    def pedir_raza_perro(self):
        return input("Ingrese la raza de su Perro\n->")
    
    def pedir_sexo_perro(self):
        return input("Ingrese el sexo de su Perro\n->")

    def pedir_tamaño_perro(self):
        return input("Ingrese el Tamaño del Perro\n->")

    def consultar_si_desea_ingresar_otro_perro(self):
        return input("Desea ingresar otro Perro?\n->[S/N]")
        
    
    def manejo_de_errores(self):
        self.limpiar_pantalla()
        self.dato_invalido()
        self.mostrar_mensaje_continuar()

    def limpiar_pantalla(self):
        time.sleep(0.5)
        os.system("cls")
    
    def dato_invalido(self):
        print("Error, dato ingresado no válido ❌.")

    def mostrar_mensaje_continuar(self):
        return input("Presiona enter para continuar ✅")

    def gracias_por_utilizar_nuestro_programa(self):
        print("Gracias Por Utilizar nuestro Programa")

    def perro_No_encontrado(self):
        print("El Perro no se encuentra en la Base de Datos")
    
    def mostrar_datos_perro(self,nombre,edad,color,raza,sexo,tamaño):
        print("Los Datos Del Perro Son \n->Nombre: {}\n->Edad: {}\n->Color: {}\n->Raza: {}\n->Sexo: {}\n->Tamaño: {}".format(nombre,edad,color,raza,sexo,tamaño))
    
    def mostrar_lista_perros(self,lista_perros):
        print("La lista de Perros es la siguiente:\n")
        for perro in lista_perros:
            print("Nombre:", perro["Nombre"])
            print("Edad:", perro["Edad"])
            print("Color:", perro["Color"])
            print("Raza:", perro["Raza"])
            print("Sexo:", perro["Sexo"])
            print("Tamaño:", perro["Tamaño"])
            print()

    def pedir_nombre_perro_buscado(self):
        return input("Ingrese el nombre de su Perro:\n->")
    

    def No_hay_perros_en_la_lista(self):
        print("No hay perros en la lista.")
        