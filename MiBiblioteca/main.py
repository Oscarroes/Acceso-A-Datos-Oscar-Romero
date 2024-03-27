from vista import Vista
from controlador import Controlador
from modelo import Modelo


def main():
    modelo = Modelo()
    controlador = Controlador(modelo)
    vista = Vista(controlador)

if __name__ == "__main__":
    main()