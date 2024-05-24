from conexion import EjecutarConsulta

if __name__ == "__main__":
    consultaEjecutar = "SELECT * FROM estudiantes WHERE codigo = '201255414-3743'"
    respuesta = EjecutarConsulta(consultaEjecutar)
    print(str(respuesta))
    print(respuesta[0][1])