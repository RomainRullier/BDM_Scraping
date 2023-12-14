import uvicorn
from fastapi import FastAPI
from db import *

# Description
description = """
API that returns scraped anime from MyAnimeList.net with filters.
"""

app = FastAPI(
    title="MyAnimeAPI",
    description=description,
    version="0.0.1",
)

database = DataBase('myanimelist')



@app.get("/animes")
async def root():
    animes = database.select_table('myanimelist')
    return animes


@app.get("/animes/{letter}")
async def get_animes(letter):
    animes = database.select_animes_by_letter('myanimelist', letter)
    return animes


if __name__ == "__main__":
    uvicorn.run("api:app", host="localhost", port=8000, reload=True)