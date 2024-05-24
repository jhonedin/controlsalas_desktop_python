import sys
sys.path.append('../controlsalas_desktop_python')
from conexion import EjecutarConsulta

consultaEjecutar = "SELECT * FROM estudiantes WHERE codigo = '201255414-3743'"
respuesta = EjecutarConsulta(consultaEjecutar)
print(str(respuesta))
print(respuesta[0][1])