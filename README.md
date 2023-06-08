# Movies Review API REST Server
A backend pyhton movies review with FastAPI and MySQL

## setup
- You can activate the virtual environment using **project/Scripts/Activate**
- To install the requirements run `pip install -r /path/to/requirements.txt`
- Use uvicorn to run the app using `uvicorn main:app -r` 

## Available endpoints
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/api/v1/users        (POST)
- http://127.0.0.1:8000/api/v1/users/login  (POST)
- http://127.0.0.1:8000/api/v1/movies       (POST)
- http://127.0.0.1:8000/api/v1/reviews      (GET, POST)
- http://127.0.0.1:8000/api/v1/reviews/{review_id}      (GET, POSt PUT, DELETE)
