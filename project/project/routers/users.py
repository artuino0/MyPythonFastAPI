
from fastapi import HTTPException, APIRouter, Response, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

from ..database import User

from ..helpers import create_jwt_token

from ..schemas import UserRequestModel, UserResponseModel, UserLoginResponseModel

router = APIRouter(prefix='/users')

@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestModel, token: HTTPAuthorizationCredentials = Depends(security)):

    if User.select().where(User.username == user.username).exists():
        raise HTTPException(409, 'El usuario ya esta registrado')

    hash_password = User.hash_password(user.password)

    myUser = User.create(
        username = user.username,
        password = hash_password
    )

    return myUser

@router.post('/login', response_model = UserLoginResponseModel)
async def login_user(credentials: HTTPBasicCredentials, response: Response):
    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(404, 'El usuario no existe')

    if User.hash_password(credentials.password) != user.password:
        raise HTTPException(401, 'La contraseña es incorrecta')
    
    response.set_cookie(key='user_id', value=user.id)
    token = create_jwt_token(user_id=user.id)

    return UserLoginResponseModel(id=user.id, username=user.username, token=token)