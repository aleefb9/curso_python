# Creando un diccionario simple
cancion = {
    'artista': 'Metallica',
    'cancion': 'Enter Sandman',
    'lanzamiento': 1992,
    'likes': 3000
}

#acceder a los elementos de un diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

artista = cancion['artista']

#Mezclar con un string
print(f'Estoy escuchando {artista}')
print(cancion)

#agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

#reemplazar valor existente
cancion['cancion'] = 'Seek & Destroy'
print(cancion)

#Eliminar un valor
del cancion['lanzamiento']
print(cancion)