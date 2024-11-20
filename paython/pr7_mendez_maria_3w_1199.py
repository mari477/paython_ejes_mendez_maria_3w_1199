class Universidad:
    def __init__(self, Nombre):
        self.Nombre = Nombre
class Carrera:
    def carrera(self, especialidad):
        self.especialidad = especialidad
class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}.")
persona = Estudiante("Harvard")
persona.carrera("Ingeniería Mecatrónica")
persona.datos("Mike", 19)
