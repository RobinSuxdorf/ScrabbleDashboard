import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

interface Game {
    game_id: number;
    start_player?: string | null;
    winner?: string | null;
}


const GameView = () => {
    const { id } = useParams<{ id: string}>();
    const [game, setGame] = useState<Game | null>(null)

    useEffect(() => {
        if (!id) return;

        fetch(`http://127.0.0.1:8000/games/${id}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Failed to fetch game.");
                }
                return response.json();
            })
            .then((data: Game) => {
                setGame(data);
            });
    }, [id]);

    if (!game) return <p>Game not found.</p>

    return (
        <div>
            <h2>Game #{game.game_id}</h2>
            <p>Start Player: {game.start_player ?? "Unknown"}</p>
            <p>Winner: {game?.winner ?? "Draw"}</p>
        </div>
    );
}

export default GameView;