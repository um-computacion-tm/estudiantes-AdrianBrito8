# class Profesor:
#     def __init__(self, param_nombre, param_email):
#         self.nombre = param_nombre
#         self.email = param_email
#         self.asistencia = 0

#     def cambiar_nombre(self, nuevo_nombre):
#         self.nombre = nuevo_nombre

#     def asistencia_clase(self):
#         self.asistencia += 1

# profesor_pepe:Profesor = Profesor("Pepe", "jose@um.edu.ar")
# print(id(profesor_pepe))
# print("el nombre es: ")
# print(profesor_pepe.nombre)
# print("el email es: ")
# print(profesor_pepe.email)
# print("su asistencia es: ")
# print(profesor_pepe.asistencia)

# print("EL PROFESOR FUE A CLASE...")
# profesor_pepe.asistencia_clase()
# profesor_pepe.asistencia_clase()
# profesor_pepe.asistencia_clase()
# profesor_pepe.asistencia_clase()
# profesor_pepe.asistencia_clase()
# profesor_pepe.asistencia_clase()
# profesor_pepe.asistencia_clase()

# print("su asistencia es: ")
# print(profesor_pepe.asistencia)

class Alumno:
    def __init__(self, param_nombre, param_email, param_carrera ):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0
        self.legajo = 1234
        self.carrera = param_carrera
        #super().__init__(param_nombre, param_email, param_carrera)
        #self.materias_cursando[]

    def asistencia_clase(self):
        self.asistencia += 1





alumno_:Alumno = Alumno("Adrian", "adrian@um.edu.ar", "Ing.Informática")
print("el nombre del alumno es:")
print(alumno_.nombre)
print("el email del alumno es:")
print(alumno_.email)
print("legajo del alumno:")
print(alumno_.legajo)
print("la carrera del alumno es:")
print(alumno_.carrera)
print("cantidad de clases asistidas por el alumno:")
alumno_.asistencia_clase()
alumno_.asistencia_clase()
print(alumno_.asistencia)