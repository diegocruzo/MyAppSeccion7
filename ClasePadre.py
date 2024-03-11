class Mamifero:
    # Crear el constructor de la clase
    def __init__(self, nombre=""):
        self.nombre = nombre

    # Constructor creado por sobrecarga de métodos
    def __init__(self):
        self.nombre = "Por definir"

    # Método para visualizar la información
    def __str__(self):
        return self.nombre
