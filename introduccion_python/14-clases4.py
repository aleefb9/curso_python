#HERENCIAS
class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo 
        self.categoria = categoria 
        self.__precio = precio # Default: PUBLIC, PROTECTED, PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.__precio}')

    #GETTERS AND SETTERS - GET = Obtiene un valor, SET = Agrega un valor
    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

#crear clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 estrellas', 200)
hotel.mostrar_informacion()