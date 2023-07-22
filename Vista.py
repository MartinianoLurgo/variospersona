


class Vista:
    def __init__(self):
        pass



    def menu(self):
        print("----------------------------------")
        print("             PERRO                ")
        print("[1] Ingresar Perro nuevo")
        print("[2] Consultar Datos de Perro")
        print("[3] Eliminar Perro de La BD")
        print("----------------------------------")
        return input("Ingrese una opcion valida por favor")

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
    
    def mostrar_lista_perros(self,lista):
        print(self.lista)
    

    def mostrar_datos_perro(self,datos):
        print(self.datos)