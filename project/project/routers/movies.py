from fastapi import APIRouter

from ..database import Movie
from ..schemas import MovieRequestModel, MovieResponseModel

router = APIRouter(prefix='/movies')

@router.post('', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
    myMovie = Movie.create(
        title = movie.title
    )
    return myMovie