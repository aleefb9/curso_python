playlist = {} #diccionario vacio
playlist['canciones'] = [] #lista vacia de canciones

#Función prinfipal
def app():
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿Cómo deseas nombrar la pLaylist?')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            #Ya tenemos un nombre, desctivamos el true
            agregar_playlist = False
            #Mandar llamar la función para aagregar canciones
            agregar_canciones()

            print(playlist)

def agregar_canciones():
    print('Agregar canciones...')

    #Bandera para aagregar canciones
    agregar_cancion = True

    while agregar_cancion:
        #Preguntar al usuario que canción desean agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)
        if cancion == 'X':
            #Dejar de agregar canciones
            agregar_cancion = False

            #Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            #agregar canciones a la playlist
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()