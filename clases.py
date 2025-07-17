# clases.py

class Estudiante:
    def __init__(self, nombre, edad, carrera, notas, beca):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = notas
        self.beca = beca
    
    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def es_aprobado(self):
        return self.calcular_promedio() >= 13

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}, Notas: {self.notas}, Beca: {'Sí' if self.beca else 'No'}"

class Becado(Estudiante):
    def __init__(self, nombre, edad, carrera, notas, beca, tipo_beca):
        super().__init__(nombre, edad, carrera, notas, beca)
        self.tipo_beca = tipo_beca

    def mostrar_datos(self):
        return super().mostrar_datos() + f", Tipo de Beca: {self.tipo_beca}"
