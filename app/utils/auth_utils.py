import jwt
import os
from dotenv import load_dotenv 
from flask import request, jsonify
from functools import wraps
from datetime import datetime, timedelta, timezone

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET")

def generate_token(user):
    payload = {
        'id': user['id'],
        'rol': user['rol'],
        'exp': datetime.now(tz=timezone.utc) + timedelta(days=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return "vencido"
    except jwt.InvalidTokenError:
        return "invalido"


def requiere_roles(*roles_permitidos):
    def decorador(funcion):
        @wraps(funcion)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if auth_header is None:
                return jsonify({"message": "Token de autenticacion no proporcionado"}), 401
            elif not auth_header.startswith('Bearer '):
                return jsonify({"message": "Token de autenticacion invalido"}), 401
            token = auth_header.split(' ')[1]
            payload = verify_token(token)

            if payload == "invalido" or payload == "vencido":
                return jsonify({"message": "Token de autenticacion invalido"}), 401
            else:
                if payload['rol'] not in roles_permitidos:
                    return jsonify({"message": "No tienes permiso para realizar esta accion"}), 403
                else:
                    return funcion(*args, **kwargs) 
        return wrapper
    return decorador
