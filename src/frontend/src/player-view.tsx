import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

interface Player {
    player_id: number;
    name: string;
}

const PlayerView = () => {
    const { id } = useParams<{ id: string}>();
    const [player, setPlayer] = useState<Player | null>(null)

    useEffect(() => {
        if (!id) return;

        fetch(`http://127.0.0.1:8000/players/${id}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Failed to fetch game.");
                }
                return response.json();
            })
            .then((data: Player) => {
                setPlayer(data);
            });
    }, [id]);

    if (!player) return <p>Player not found.</p>

    return (
        <div>
            <p>Player ID #{player.player_id}</p>
            <p>Name: {player.name}</p>
        </div>
    );
}

export default PlayerView;