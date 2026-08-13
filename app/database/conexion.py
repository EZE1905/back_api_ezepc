import psycopg2

def conectar_base_datos():
    try:
        connection = psycopg2.connect(
            user="eze_pc",
            password="eze_pc",
            host="127.0.0.1",
            port="5432",
            database="eze_pc")
        cursor = connection.cursor()
        print("Conexión exitosa a la base de datos")
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos", error)
    return connection, cursor

def cerrar_base_datos(connection, cursor):
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Conexión a la base de datos cerrada")
    