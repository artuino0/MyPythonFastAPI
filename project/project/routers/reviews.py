from fastapi import HTTPException, APIRouter
from ..schemas import ReviewResponseModel, ReviewRequestModel, ReviewRequestPutModel
from ..database import User, Movie, UserReview

router = APIRouter(prefix='/reviews')

@router.post('', response_model=ReviewResponseModel)
async def create_review(user_reviewReq: ReviewRequestModel):

    if not User.select().where(User.id == user_reviewReq.user_id).exists():
        raise HTTPException(404, 'No se encontro el usuario')
    
    if not Movie.select().where(Movie.id == user_reviewReq.movie_id).exists():
        raise HTTPException(404, 'No se encontro la pelicula')
    
    user_review = UserReview.create(
        user = user_reviewReq.user_id,
        movie = user_reviewReq.movie_id,
        review = user_reviewReq.review,
        score = user_reviewReq.score
    )
    return user_review

@router.get('', response_model=list[ReviewResponseModel])
async def get_reviews(page: int = 1, limit: int = 10):
    return list(UserReview.select().paginate(page, limit))

@router.get('/{review_id}', response_model=ReviewResponseModel)
async def get_review(review_id: int):
    review = UserReview.select().where(UserReview.id == review_id).first()
    if not review:
        raise HTTPException(404, 'No se encontro la reseña')
    return review

@router.put('/{review_id}', response_model=ReviewResponseModel)
async def update_review(review_id: int, review_req: ReviewRequestPutModel):
    review = UserReview.select().where(UserReview.id == review_id).first()

    if not review:
        raise HTTPException(404, 'No se encontro la reseña')
    
    review.review = review_req.review
    review.score = review_req.score
    review.save()
    return review

@router.delete('/reviews/{review_id}')
async def delete_review(review_id: int):
    review = UserReview.select().where(UserReview.id == review_id).first()

    if not review:
        raise HTTPException(404, 'No se encontro la reseña')
    
    review.delete_instance()
    return {'message': 'Se elimino la reseña'}
