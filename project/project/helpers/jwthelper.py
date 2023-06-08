import jwt
from jwt import PyJWTError
from fastapi import HTTPException
from datetime import datetime, timedelta

SECRET_KEY = "MiPoderosaScretKey"
ALGORITHM = "HS256"

def create_jwt_token(user_id: int) -> str:
    payload = {'user_id': user_id, 'exp': datetime.utcnow() + timedelta(minutes=120)}
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token

def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido")