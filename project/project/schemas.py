from pydantic import BaseModel
from pydantic import validator
from typing import Any
from pydantic.utils import GetterDict
from peewee import ModelSelect

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any=None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res
    
class ReviewValidator():
    @validator('score')
    def score_validator(cls, score):
        if score < 1 or score > 5:
            raise ValueError('La calificacion debe estar entre 1 y 5')
        return score

class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('El nombre de usuario debe tener entre 3 y 50 caracteres')
        return username
        
    @validator('password')
    def password_validator(cls, password):
        if len(password) < 3 or len(password) > 50:
            raise ValueError('La contraseña debe tener entre 3 y 50 caracteres')
        return password
    
class ReviewRequestModel(BaseModel,ReviewValidator):
    user_id: int
    movie_id: int
    review: str
    score: int
    

class MovieRequestModel(BaseModel):
    title: str

    @validator('title')
    def title_validator(cls, title):
        if len(title) < 3 or len(title) > 50:
            raise ValueError('El titulo debe tener entre 3 y 50 caracteres')
        return title
    
class UserResponseModel(ResponseModel):
    id: int
    username: str

class UserLoginResponseModel(ResponseModel):
    id: int
    username: str
    token: str


    
class MovieResponseModel(ResponseModel):
    id: int
    title: str


class ReviewResponseModel(ResponseModel):
    id: int
    user: UserResponseModel
    movie: MovieResponseModel
    review: str
    score: int

class ReviewRequestPutModel(BaseModel, ReviewValidator):
    review: str
    score: int

    
