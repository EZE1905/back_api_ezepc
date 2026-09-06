from app.database.conexion import conectar_base_datos, cerrar_base_datos


def ver_todas_las_ventas():
    connection, cursor = conectar_base_datos()
    cursor.execute("SELECT * FROM ventas")
    ventas = cursor.fetchall()
    cerrar_base_datos(connection, cursor)
    return ventas

def crear_venta_nueva(data):
    connection, cursor = conectar_base_datos()
    try:
        id_usuario = data['id_usuario']
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = (%s)", (id_usuario,))
        usuario = cursor.fetchone()
        if usuario is None:
            return 'usuario no encontrado'
        else: 
            productos = data['productos']
            total = 0
            productos_validados = []
            for producto_json in productos:
                id_producto = producto_json['id_producto']
                cursor.execute("SELECT * FROM productos WHERE id_producto = (%s)", (id_producto,))
                producto_db = cursor.fetchone()
                if producto_db is None:
                    return 'producto no encontrado'
                else:
                    cantidad = producto_json['cantidad']
                    if cantidad <= 0:
                        return 'cantidad no válida'
                    if producto_db[4] < cantidad:
                        return 'stock insuficiente'
                    else:
                        precio = producto_db[3]
                        total += precio * cantidad
                        productos_validados.append((id_producto, cantidad, precio))
            cursor.execute("INSERT INTO ventas (id_usuario, total) VALUES (%s, %s) RETURNING id_venta", (id_usuario, total))
            id_venta = cursor.fetchone()[0]
            for producto in productos_validados:
                id_producto, cantidad, precio = producto
                cursor.execute("INSERT INTO detalle_ventas (id_venta, id_producto, cantidad, precio) VALUES (%s, %s, %s, %s)", (id_venta, id_producto, cantidad, precio))
                cursor.execute("UPDATE productos SET stock = stock - %s WHERE id_producto = %s", (cantidad, id_producto))
            connection.commit()
            return True
    except Exception as e:
        connection.rollback()
        print("Error al crear la venta:", e)
        return False
    finally:
        cerrar_base_datos(connection, cursor)