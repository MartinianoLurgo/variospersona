from Controlador import Controlador
import time
import os

if __name__ == "__main__":
    controller = Controlador()
    controller.Vista.limpiar_pantalla()
    controller.ejecutar_menu()