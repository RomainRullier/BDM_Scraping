import uvicorn
from fastapi import FastAPI

# Description of the API
description = """
This is your app description, written in markdown code 

# This is a title 

* This is a bullet point

"""

tag_metadata = [
    {
        "name": "GET",
        "description": "Operations with GET methods. ",
    },
    {
        "name": "TEST",
        "description": "Operations with POST methods. ",
    },
]

app = FastAPI(
    description=description,
    tag_metadata=tag_metadata
)

@app.get('/', tags=['GET'])
def index():
    return "Hello World"

@app.get('/square', tags=['TEST'])
def square(n):
    return {n: int(n)**2}


if __name__ == '__main__':
    uvicorn.run(app=app, 
                host='localhost',
                port=8000)