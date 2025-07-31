import contextlib
import sqlite3
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


class Game(BaseModel):
    game_id: int
    winner: str | None

@contextlib.contextmanager
def get_connection(db_path: str = "scrabble.db")-> sqlite3.Connection:
    conn: sqlite3.Connection = sqlite3.connect(db_path)

    try:
        yield conn
    finally:
        conn.close()

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


@app.get("/games", response_model=list[Game])
async def get_games() -> list[Game]:
    try:
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            response = conn.execute("""
                SELECT g.game_id, p.name as winner
                FROM games g
                LEFT JOIN players p ON p.player_id = g.winner
            """)

            return [Game(**dict(row)) for row in response.fetchall()]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching  games: {e}")
