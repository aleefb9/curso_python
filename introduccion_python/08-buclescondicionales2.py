# Operadores and y or
usuario_logueado = True
usuario_admin = True

#AND
if usuario_logueado and usuario_admin:
    print('ADMINISTRADOR')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes Iniciar sesión')

#OR
if usuario_logueado or usuario_admin:
    print('ADMINISTRADOR')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes Iniciar sesión')