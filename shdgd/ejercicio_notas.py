notas = []

def menu ():
    print("Opciones: ")
    print("1 Añadir nuevas calificaciones : ")
    print("2 Nota Media ")
    print("3 Nota más alta ")
    print("4 Nota más baja ")
    print("5 Salir ")
    
    
def nuevas_notas(notas):
    nota = (input("Dime la nota : "))
    notas.append(nota)
    return notas

def nota_media(notas):
    media = notas/len(notas)
    print("La nota media es",media)
    return notas 
    
    
def notamásalta(notas):
    nota_maxima = max(notas)
    print("La nota más alta es", nota_maxima)
    return notas
    
    
def notamásbaja(notas):
    nota_minima = min(notas)
    print("La nota más baja es", nota_minima)
    return notas
    
    
    
    while True:
        opcion = menu()
        if opcion == 1:
            nuevas_notas(notas)      
        elif opcion == 2:
            nota_media(notas) 
        elif opcion == 3:
            notamásalta(notas) 
        elif opcion == 4:
            notamásbaja(notas)
            break
        
    

    
