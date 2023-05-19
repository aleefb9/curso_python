def informacion(nombre, puesto = 'Desconocido'):
    # Para que nos coja los valores entre las llaves, debemos de poner una f al inicio
    print(f'Soy {nombre} y soy {puesto} ')

informacion('Alejandro', 'Programador')
informacion('Cristian', 'carnicero')
# Cuando no haya valor en la segunda variable pillará el valor por defecto
informacion('Manolo')
