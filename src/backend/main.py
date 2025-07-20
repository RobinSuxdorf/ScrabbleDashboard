import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    try:
        with sqlite3.connect("scrabble.db") as conn:
            response = conn.execute("""
                SELECT name
                FROM players
            """)

            result = response.fetchall()
            players = [r[0] for r in result]
            return {"players": players}
    except Exception as e:
        return {"message": f"Error while fetching players: {e}"}
