libros_disponibles = ["Libro 1","Libro 2","Libro 3","Libro 4","Libro 5"]
libros_prestados = []


def menu():
    print("Opciones: ")
    print("1 Ver Libros Disponibles ")
    print("2 Prestar Libro ")
    print("3 Devolver Libro ")
    print("4 Salir ")
#menu()

def verlibros ():
    for verlibros in libros_disponibles:
        print(verlibros)
#verlibros()
    