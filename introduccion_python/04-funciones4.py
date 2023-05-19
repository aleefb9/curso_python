# FUNCIONES Y MÉTODOS

nombre = 'Alejandro'

# FUNCIONES
def mostrar_nombre(nombre):
    print(f'Hola {nombre}')

mostrar_nombre(nombre)

# MÉTODOS
print( nombre.upper() )
print( nombre.title() )

# RETO
mensaje = 'Bienvenido'

def escribir_mensaje(mensaje):
    print(mensaje)

def escribir_mensaje2(mensaje):
    print(f'{mensaje}, {nombre}')

escribir_mensaje(mensaje)
escribir_mensaje2(mensaje)