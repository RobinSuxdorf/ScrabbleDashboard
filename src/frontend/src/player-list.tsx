import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

interface Player {
    player_id: number;
    name: string;
}

const PlayerList = () => {
    const [data, setData] = useState<Player[]>([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/players/")
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data: Player[]) => setData(data))
            .catch((error) => console.error("Fetch error:", error));
    }, []);

    return (
        <table>
            <thead>
                <tr>
                    <th>Player ID</th>
                    <th>Name</th>
                </tr>
            </thead>
            <tbody>
                {data.length > 0 ? (
                    data.map((p: Player) => (
                        <tr key={p.player_id}>
                            <td>
                                <Link to={`/players/${p.player_id}`}>
                                    {p.player_id}
                                </Link>
                            </td>
                            <td>{p.name}</td>
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

export default PlayerList;
