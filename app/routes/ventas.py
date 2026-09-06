from flask import Blueprint, jsonify, request
from app.servicios.venta_service import crear_venta_nueva, ver_todas_las_ventas

ventas_bp = Blueprint('ventas', __name__)

@ventas_bp.get('/ventas')
def ventas():
    ventas = ver_todas_las_ventas()
    return jsonify(ventas) 

@ventas_bp.post('/ventas')
def crear_venta():
    data = request.get_json()

    venta = crear_venta_nueva(data)

    if venta == 'usuario no encontrado':
        return jsonify({"message": "usuario no encontrado"}), 500
    elif venta == 'producto no encontrado':
        return jsonify({"message": "producto no encontrado"}), 500
    elif venta == 'cantidad no válida':
        return jsonify({"message": "cantidad no válida"}), 500
    elif venta == 'stock insuficiente':
        return jsonify({"message": "stock insuficiente"}), 500
    else:
        return jsonify({"message": "Venta creada correctamente"}), 201
        


###### EJEMPLO DE DATA PARA CREAR UNA VENTA #######
"""
{
  "id_usuario": 3,
  "productos": [
    {"id_producto": 11, "cantidad": 2},
    {"id_producto": 17, "cantidad": 1}
  ]
}
"""