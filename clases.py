# clases.py

class Estudiante:
    contador_id = 1

    def __init__(self, nombre, edad, carrera, notas, beca):
        self.id = Estudiante.contador_id
        Estudiante.contador_id += 1
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = notas
        self.beca = beca
    
    def calcular_promedio(self):
        return round(sum(self.notas) / len(self.notas), 2)

    def es_aprobado(self):
        return self.calcular_promedio() >= 13

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}, Notas: {self.notas}, Beca: {'Sí' if self.beca else 'No'}"

    @staticmethod
    def validar_notas(notas):
        return all(0 <= nota <= 20 for nota in notas)

class Becado(Estudiante):
    def __init__(self, nombre, edad, carrera, notas, beca, tipo_beca):
        super().__init__(nombre, edad, carrera, notas, beca)
        self.tipo_beca = tipo_beca

    def mostrar_datos(self):
        return super().mostrar_datos() + f", Tipo de Beca: {self.tipo_beca}"
