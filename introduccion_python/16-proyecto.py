import os

CARPETA = 'contactos/' # carpeta de contactos
EXTENSION = '.txt' # extensión de archivos

# Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    # revisa si la carpeta existe o no
    crear_directorio()

    # muestra el menú de opciones
    mostrar_menu()

    # preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            ver_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida, intente de nuevo')


def agregar_contacto():
    print('-----AGREGAR CONTACTOS-----\r\n')
    print('Escribe los datos para agregar el nuevo contacto: ')
    nombre_contacto = input('Nombre del contacto:\r\n')

    # revisar si el archivo ya existe antes de crearlo
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # resto de los campos
            telefono_contacto = input('Agrega el Teléfono:\r\n')
            categoria_contacto = input('Categoría Contacto:\r\n')

            # instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            # mostrar un mensaje de éxito
            print('\r\n CONTACTO CREADO CORRECTAMENTE \r\n')

    else: 
        print('Ese contacto ya existe')

    # reiniciar la app
    app()


def editar_contacto():
    print('-----EDITAR CONTACTOS-----\r\n')
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar:\r\n')

    # revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            # resto de los campos
            nombre_contacto = input('Agrega el nuevo nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo telefono: \r\n')
            categoria_contacto = input('Agrega la nueva categoria: \r\n')

            # instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

        # renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

        # mostrar mensaje de éxito
        print('\r\n CONTACTO EDITADO CORRECTAMENTE \r\n')

    else:
        print('Ese contacto no existe')

    # reiniciar la aplicación
    app()


def ver_contacto():
    print('-----VER CONTACTOS-----\r\n')  
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # imprime los contenidos
                print(linea.rstrip())
            #imprime un separador entre contactos
            print('\r\n')


def buscar_contacto():
    print('-----BUSCAR CONTACTOS-----\r\n')
    nombre = input('Seleccione el Contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)

    #reiniciar la aplicación
    app()


def eliminar_contacto():
    print('-----ELIMINAR CONTACTOS-----\r\n') 
    nombre = input('Seleccione el Contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado correctamente')
    except:
        print('No existe ese contacto')

    # reiniciar la app
    app()


def mostrar_menu():
    print('Seleccione en el Menú lo que desea hacer')  
    print('1. Agregar Nuevo Contacto') 
    print('2. Editar Contacto') 
    print('3. Ver Contactos') 
    print('4. Buscar Contactos') 
    print('5. Eliminar Contactos') 


def crear_directorio():
    if not os.path.exists('contactos/'):
        # crear la carpeta
        os.makedirs('contactos/')
    else:
        print('La carpeta ya existe')


def existe_contacto(nombre):
    # revisar si el archivo ya existe antes de crearlo
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()