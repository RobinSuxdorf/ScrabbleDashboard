import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';

interface Game {
    game_id: number;
    start_player?: string | null;
    winner?: string | null;
}

interface PlayerScore {
    player_id: number;
    name: string;
    score: number;
}

interface GameDetails {
    game: Game;
    player_scores: PlayerScore[];
}

const GameView = () => {
    const { id } = useParams<{ id: string}>();
    const [gameDetails, setGameDetails] = useState<GameDetails | null>(null)

    useEffect(() => {
        if (!id) return;

        fetch(`http://127.0.0.1:8000/games/${id}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Failed to fetch game.");
                }
                return response.json();
            })
            .then((data: GameDetails) => {
                setGameDetails(data);
            });
    }, [id]);

    if (!gameDetails) return <p>Game not found.</p>

    return (
        <div>
            <h2>Game #{gameDetails.game.game_id}</h2>
            <p>Start Player: {gameDetails.game.start_player ?? "Unknown"}</p>
            <p>Winner: {gameDetails.game.winner ?? "Draw"}</p>

            <h3>Player Scores</h3>
            <table>
                <thead>
                    <tr>
                        <th>Player ID</th>
                        <th>Name</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
                    {gameDetails.player_scores.map((score: PlayerScore) => (
                        <tr key={score.player_id}>
                            <td>
                                <Link to={`/players/${score.player_id}`}>
                                    {score.player_id}
                                </Link>
                            </td>
                            <td>{score.name}</td>
                            <td>{score.score}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default GameView;