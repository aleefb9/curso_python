def app():
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip()) # rstrip elimina los saltos de línea generados por el compilador

app()