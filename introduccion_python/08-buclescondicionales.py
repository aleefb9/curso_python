# OPERADORES CONDICIONALES
    #  == IGUAL 
    # != DISTINTO
    # > MAYOR QUE
    # >= MAYOR O IGUAL QUE
    # < MENOR QUE
    # <= MENOR O IGUAL QUE

#Revisar si una condición es mayor a
balance = 500
if balance > 501:
    print('puedes pagar')
else:
    print('no tienes saldo suficiente')

#Likes
likes = 200
if likes == 200:
    print('Excelente, 200 likes')
else: 
    print('Casu llegas a los 200')

#IF con texto
lenguaje = 'Python'
if lenguaje == "Python":
    print('Excelente decisión')

if not lenguaje == "PHP":
    print('Mala decisión')

#Evaluar un Boolean
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado == True:
    if usuario_admin:
        print('Acceso al sistema')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesión')


#Evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

if 'PHP' in lenguajes:
    print('PHP Si existe')
else:
    print('PHP No existe')