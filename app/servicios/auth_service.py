from app.database.conexion import conectar_base_datos, cerrar_base_datos
from werkzeug.security import generate_password_hash, check_password_hash

def registrar_usuario(data):
    nombre = data['nombre']
    email = data['email']
    password = data['password']
    rol = data['rol']

    # Verificar si el correo electrónico ya está registrado
    connection, cursor = conectar_base_datos()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        cerrar_base_datos(connection, cursor)
        return True
    else:
        # Encriptar la contraseña
        hashed_password = generate_password_hash(password)
        # Guardar el usuario en la base de datos
        cursor.execute("INSERT INTO usuarios (nombre, email, password, rol) VALUES (%s, %s, %s, %s)", (nombre, email, hashed_password, rol))
        connection.commit()
        cerrar_base_datos(connection, cursor)
        return False

def login_usuario(data):
    email = data['email']
    password = data['password']

    connection, cursor = conectar_base_datos()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if not existing_user:
        cerrar_base_datos(connection, cursor)
        return False
    else:
        hashed_password = existing_user[3]
        if check_password_hash(hashed_password, password):
            cerrar_base_datos(connection, cursor)
            return True
        else:
            cerrar_base_datos(connection, cursor)
            return False