import jwt
import os
from dotenv import load_dotenv 

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