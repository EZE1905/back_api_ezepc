from app.database.conexion import conectar_base_datos, cerrar_base_datos

def mostrar_todos_los_productos():
    connection, cursor = conectar_base_datos()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    cerrar_base_datos(connection, cursor)
    return productos

def crear_producto_nuevo(request_data):
    connection, cursor = conectar_base_datos()
    cursor.execute("INSERT INTO productos (nombre, descripcion, precio, stock, categoria) VALUES (%s, %s, %s, %s, %s)", (request_data['nombre'], request_data['descripcion'], request_data['precio'], request_data['stock'], request_data['categoria']))
    connection.commit()
    cerrar_base_datos(connection, cursor)
    return True

def mostrar_un_producto(producto_id):
    connection, cursor = conectar_base_datos()
    cursor.execute("SELECT * FROM productos WHERE id_producto = %s", (producto_id,))
    producto = cursor.fetchone()
    cerrar_base_datos(connection, cursor)
    return producto

def actualizar_un_producto(producto_id, request_data):
    connection, cursor = conectar_base_datos()
    cursor.execute("UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, stock = %s, categoria = %s WHERE id_producto = %s",
                (request_data['nombre'], request_data['descripcion'], request_data['precio'], request_data['stock'], request_data['categoria'], producto_id))
    connection.commit()
    cerrar_base_datos(connection, cursor)
    validacion = cursor.rowcount
    return validacion

def eliminar_un_producto(producto_id):
    connection, cursor = conectar_base_datos()
    cursor.execute("DELETE FROM productos WHERE id_producto = %s", (producto_id,))
    connection.commit()
    cerrar_base_datos(connection, cursor)
    validacion = cursor.rowcount
    return validacion