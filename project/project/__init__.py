from fastapi import FastAPI, APIRouter
from fastapi import HTTPException

from .routers import user_router, movie_router, review_router

from .database import User
from .database import Movie
from .database import UserReview
from .database import database as connection

app = FastAPI(title='Proyecto de reseña de peliculas', description='En este proyecto seremos capaces de reseñar peliculas', version='1.0')

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router, tags=['Users'])
api_v1.include_router(movie_router, tags=['Movies'])
api_v1.include_router(review_router, tags=['Reviews'])

app.include_router(api_v1)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
        print('Connecting..')
    connection.create_tables([User, Movie, UserReview])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        print('Closing..')


