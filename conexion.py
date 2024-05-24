import mysql.connector

def EjecutarConsulta(consulta):
    try:
        # Establecer la conexión a la base de datos MySQL
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="jhon",
            password="UnivalleTulua2023**",
            database="bdcontrolasistenciasalas"
        )

        if conexion.is_connected():
            #print("Conexión establecida correctamente")

            # Ejemplo de consulta
            cursor = conexion.cursor()
            #cursor.execute("SELECT * FROM estudiantes WHERE codigo = '201255414-3743'")
            cursor.execute(consulta)
            filas = cursor.fetchall()

            # Imprimir los resultados
            #for fila in filas:
            #    print(fila)

            # Cerrar cursor y conexión
            cursor.close()
            #print("Cursor cerrado correctamente")
            conexion.close()
            #print("Conexión cerrada correctamente")
            return filas

    except mysql.connector.Error as error:
        print("Error al conectarse a la base de datos:", error)
