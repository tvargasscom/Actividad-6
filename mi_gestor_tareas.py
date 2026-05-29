def obtener_tareas():
    """
    En esta función creamos la lista inicial de tareas para empezar el programa
    y se retorna una lista con 3 diccionarios (las tareas).
    """
    # hago la lista inicial con las 3 tareas de ejemplo
    lista = [
        {"descripcion": "Leer un libro", "completada": True},
        {"descripcion": "Lavar la loza", "completada": False},
        {"descripcion": "Sacar a pasear al perro", "completada": False}
    ]
    return lista

def mostrar_tareas(lista_tareas):
    """
    esta función recibe como parámetro la lista de tareas y la muestra en la terminal con numeros,
    no retorna nada.
    """
    print("\n Mis Tareas:")
    
    # acá recorro la lista usando el tamaño de la lista para tener el indice i
    for i in range(len(lista_tareas)):
        tarea = lista_tareas[i]
        
        # acá veo si le coloco la X o la dejo vacia dependiendo de si la tarea esta hecha o no basandome en el booleano que retorna de la clave del diccionario
        if tarea["completada"] == True:
            estado = "(X)"
        else:
            estado = "( )"
        
        # acá se muestran los números de lista empezando desde 0, lo dejo así para que sea más fácil manejar los elementos de la lista.
        print(f"{i}. {estado} {tarea['descripcion']}")
        
    print("------------------")

def agregar_tarea(lista_tareas, descripcion):
    """
    Esta función agrega una tarea al final de la lista, toma como parámetros la lista de tareas que es la lista donde se va a guardar y la descripción que es el texto que dice lo que hay que hacer y retorna la lista actualizada.
    
    """
    nueva = {"descripcion": descripcion, "completada": False}
    lista_tareas.append(nueva)
    print("Tarea agregada.")
    return lista_tareas

def marcar_completada(lista_tareas, posicion):
    """
    Esta función busca la tarea por su número y le cambia el estado a completada, toma como parametros lista_tareas y el número de la posición del elemento de la lista que queremos modificar, no retorna nada.

    """
    #acá usamos un try except por si el usuario llega a poner un número que no es válido por si se pasa del tamaño de la lista
    try:
        lista_tareas[posicion]["completada"] = True
        print("la tarea se marcó correctamente como hecha")
    except IndexError:
        print("Esa posicion no existe, intente con un número válido.")
        
        
def contar_tareas_pendientes(lista_tareas, indice=0):
    """
    Esta función cuenta recursivamente cuántas tareas faltan por hacer, toma como parámetros lista_tareas que es la lista con los diccionarios y también toma el índice cuyo valor por defecto lo puse en 0 y retorna el número de tareas pendientes.
    
    """
    # Caso Base: si el índice ya llegó al final de la lista, se corta recursividad la y se devuelve 0
    if indice == len(lista_tareas):
        return 0
    
    # Caso Recursivo: se mira la tarea en la posición del indice actual
    tarea_actual = lista_tareas[indice]
    
    if tarea_actual["completada"] == False:
        # como la tarea esta pendiente, le sumo 1 al contador y llamo a esta misma función sumando 1 al índice
        return 1 + contar_tareas_pendientes(lista_tareas, indice + 1)
    else:
        # como la tarea ya esta hecha, no sumo nada y sigo con la siguiente posición.
        return contar_tareas_pendientes(lista_tareas, indice + 1)

# acá se empieza el flujo principal del programa
if __name__ == "__main__":
    # acá se piden las tareas iniciales llamando a la funcion
    mis_tareas = obtener_tareas()
    
    # acá se arma el menú infinito con el uso de un bucle while
    while True:
        print("\n  Menú  ")
        print("1) Ver tareas")
        print("2) Añadir una tarea")
        print("3) Marcar una tarea completada")
        print("4) Ver tareas pendientes")
        print("5) Salir")
        
        opcion = input("Elija una opción (1-5): ")
        
        if opcion == "1":
            mostrar_tareas(mis_tareas)
            
        elif opcion == "2":
            texto = input("Escriba la descripcion de la tarea: ")
            mis_tareas = agregar_tarea(mis_tareas, texto)
            
        elif opcion == "3":
            mostrar_tareas(mis_tareas)
            try:
                # acá se pide el número de la tarea ya completada y se convierte el número a entero
                num = int(input("Que número de tarea ya terminó? "))
                marcar_completada(mis_tareas, num)
            except ValueError:
                # acá manejamos el caso en el que el usuario no escriba un número
                print("Por favor escriba un número entero.")
                
        elif opcion == "4":
            # se llama a la funcion recursiva
            faltan = contar_tareas_pendientes(mis_tareas)
            print(f"Te faltan {faltan} tareas por terminar.")
            
        elif opcion == "5":
            print("Ha salido correctamente del programa.")
            break # se rompe el bucle while para poder salir
            
        else:
            print("Opción no válida, porfavor escriba un número entre 1 y 5")