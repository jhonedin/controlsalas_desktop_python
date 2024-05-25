import sys
sys.path.append('../controlsalas_desktop_python')
from conexion import EjecutarConsulta

class EstudianteModel:
    def __init__(self, idusuario, codigo, nombre, correo, clave, direccion, perfil, estado):
        self.idusuario = idusuario
        self.codigo = codigo
        self.nombre = nombre
        self.correo = correo
        self.clave = clave
        self.direccion = direccion
        self.perfil = perfil
        self.estado = estado

    def getEstudiante(self,codigo):
        consultaEjecutar = f"SELECT * FROM estudiantes WHERE codigo = '{codigo}'"
        #print(consultaEjecutar)
        respuesta = EjecutarConsulta(consultaEjecutar)
        return respuesta
    
    def getEstudiantesList(self):
        consultaEjecutar = "SELECT * FROM estudiantes"
        respuesta = EjecutarConsulta(consultaEjecutar)
        return respuesta


# ---- PRUBAS DE LA CLASE ESTUDIANTE ----
estudiante1 = EstudianteModel(idusuario=1, codigo='2021001', nombre='Juan Perez', correo='juan.perez@example.com',
                              clave='1234', direccion='Calle Falsa 123', perfil='Estudiante', estado='activo')

print("\n -- Probando la funcion getEstudiante \n")
un_codigo = '201255414-3743'
respuesta_consulta = estudiante1.getEstudiante(un_codigo)
print(str(respuesta_consulta))
print(respuesta_consulta[0][1])

print("\n -- Probando la funcion getEstudiantes \n")
respuesta_consulta2 = estudiante1.getEstudiantesList()
print(str(respuesta_consulta2))
print("\n")
for fila in respuesta_consulta2:
    print(fila)
print("\n")
for fila in respuesta_consulta2:
    print("Fila:")
    for dato in fila:
        print(dato)
    print("-" * 50)  # Separador entre filas

#consultaEjecutar = "SELECT * FROM estudiantes WHERE codigo = '201255414-3743'"
#respuesta = EjecutarConsulta(consultaEjecutar)
#print(str(respuesta))
#print(respuesta[0][1])



