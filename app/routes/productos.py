from flask import Blueprint, jsonify, request
from app.servicios.producto_servicio import mostrar_todos_los_productos, crear_producto_nuevo, mostrar_un_producto, actualizar_un_producto, eliminar_un_producto
from app.utils.auth_utils import verify_token, requiere_roles

productos_bp = Blueprint('productos', __name__)

@productos_bp.get('/productos')
def productos():
    productos = mostrar_todos_los_productos()
    return jsonify(productos)

@productos_bp.post('/productos')
@requiere_roles('empleado', 'admin')
def crear_producto():
    request_data = request.get_json()
    crear_producto_nuevo(request_data)
    return jsonify({"message": "Producto creado correctamente"}), 201

@productos_bp.get('/productos/<int:producto_id>')
def mostrar_producto(producto_id):
    producto = mostrar_un_producto(producto_id)
    if not producto:
        return jsonify({"message": "Producto no encontrado"}), 404
    return jsonify(producto)

@productos_bp.put('/productos/<int:producto_id>')
@requiere_roles('empleado', 'admin')
def actualizar_producto(producto_id):
    request_data = request.get_json()
    validacion = actualizar_un_producto(producto_id, request_data)
    if validacion == 0:
        return jsonify({"message": "Producto no encontrado"}), 404
    elif validacion > 0:
        return jsonify({"message": "Producto actualizado correctamente"}), 200
    else:
        return jsonify({"message": "Error al actualizar el producto"}), 500

@productos_bp.delete('/productos/<int:producto_id>')
@requiere_roles('empleado', 'admin')
def eliminar_producto(producto_id):
    validacion = eliminar_un_producto(producto_id)
    if validacion == 0:
        return jsonify({"message": "Producto no encontrado"}), 404
    elif validacion > 0:
        return jsonify({"message": "Producto eliminado correctamente"}), 200
    else:
        return jsonify({"message": "Error al eliminar el producto"}), 500
