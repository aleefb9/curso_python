numero = 0

while numero <= 10:
    print(numero)
    numero += 1 #incremento para evitar loop infinito

#IF DENTRO DE UN WHILE
while numero <= 10:
    if numero == 5:
        print('CINCOOOO!!')
        # break
    else:
        print(numero)
    numero += 1 