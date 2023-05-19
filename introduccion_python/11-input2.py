pregunta = 'Agrega un nuumero y te diré si es par o no \r\n'
pregunta += ' (Escribe "cerrar" para salir de la aplicación)'

preguntar = True

while preguntar:

    #Mezclarlo con operadores
    numero = input(pregunta)
    
    if numero == 'cerrar':
        Preguntar = False
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print(f'El número {numero} es par')
        else: 
            print(f'El número {numero} es inpar')