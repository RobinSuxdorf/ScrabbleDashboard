import { useEffect, useState } from 'react';
import './App.css'

interface Game {
    game_id: number;
    winner?: string | null;
}

function App() {
    const [data, setData] = useState<Game[]>([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/games")
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => setData(data))
            .catch((error) => console.error("Fetch error:", error));
    }, []);

    return (
    <>
        {data.length > 0 ? (
            <ul>
                {data.map((g: Game) => (
                    <li key={g.game_id}>
                        Game #{g.game_id} - Winner: {g.winner ?? "Draw"}
                    </li>
                ))}
            </ul>
        ) : (
            <p>Loading players...</p>
        )}
    </>
     )
}

export default App
