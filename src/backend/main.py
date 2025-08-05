import contextlib
import sqlite3
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


class Game(BaseModel):
    game_id: int
    start_player: str | None
    winner: str | None

class PlayerScore(BaseModel):
    player_id: int
    name: str
    score: int

class GameDetails(BaseModel):
    game: Game
    player_scores: list[PlayerScore]

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


@app.get("/games/", response_model=list[Game])
async def get_games() -> list[Game]:
    try:
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            response = conn.execute("""
                SELECT 
                    g.game_id,
                    sp.name AS start_player,
                    wp.name AS winner
                FROM games g
                LEFT JOIN players sp ON sp.player_id = g.started_by
                LEFT JOIN players wp ON wp.player_id = g.winner
            """)

            return [Game(**dict(row)) for row in response.fetchall()]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching games: {e}")

@app.get("/games/{game_id}", response_model=GameDetails)
async def get_game(game_id: int) -> GameDetails:
    try:
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            game_row = conn.execute("""
                SELECT 
                    g.game_id,
                    sp.name AS start_player,
                    wp.name AS winner
                FROM games g
                LEFT JOIN players sp ON sp.player_id = g.started_by
                LEFT JOIN players wp ON wp.player_id = g.winner
                WHERE g.game_id = ?
            """, (game_id,)).fetchone()


            if game_row is None:
                raise HTTPException(status_code=404, detail=f"Game with ID {game_id} not found.")

            game = Game(**dict(game_row))

            scores = conn.execute("""
                SELECT 
                    gs.player_id, 
                    p.name,
                    gs.score
                FROM game_scores gs
                INNER JOIN players p ON p.player_id = gs.player_id
                WHERE game_id = ?
            """, (game_id,)).fetchall()

            player_scores = [PlayerScore(**dict(score)) for score in scores]

            return GameDetails(game=game, player_scores=player_scores)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching game: {e}")
