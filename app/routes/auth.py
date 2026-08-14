from flask import Blueprint, jsonify, request
from app.database.conexion import conectar_base_datos, cerrar_base_datos
from app.servicios.auth_service import registrar_usuario,login_usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.post('/register')
def register():
    data = request.get_json()

    existing_user = registrar_usuario(data)

    if existing_user:
        return jsonify({"message": "El correo electronico ya esta registrado"}), 400
    else:
        return jsonify({"message": "Usuario registrado correctamente"}), 201

@auth_bp.post('/login')
def login():
    data = request.get_json()

    existing_user = login_usuario(data)

    if existing_user:
        return jsonify({"message": "Login exitoso"}), 200
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401

@auth_bp.get('/usuarios')
def ver_usuarios():
    connection, cursor = conectar_base_datos()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cerrar_base_datos(connection, cursor)
    return jsonify(usuarios)