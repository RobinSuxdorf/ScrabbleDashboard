import { useEffect, useState } from 'react';
import './App.css';

interface Game {
    game_id: number;
    start_player?: string | null;
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
            .then((data: Game[]) => setData(data))
            .catch((error) => console.error("Fetch error:", error));
    }, []);

    // useEffect(() => {
    //     console.log(data);
    // }, [data]);

    return (
        <table>
            <thead>
                <tr>
                    <th>Spiel</th>
                    <th>Startspieler</th>
                    <th>Sieger</th>
                </tr>
            </thead>
            <tbody>
                {data.length > 0 ? (
                    data.map((g) => (
                        <tr key={g.game_id}>
                            <td>{g.game_id}</td>
                            <td>{g.start_player ?? ""}</td>
                            <td>{g.winner ?? "Draw"}</td>
                        </tr>
                    ))
                ) : (
                    <tr>
                        <td colSpan={3}>Loading games...</td>
                    </tr>
                )}
            </tbody>
        </table>
    );
}

export default App;
