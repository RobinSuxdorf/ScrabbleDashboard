import { useEffect, useState } from 'react';
import './App.css'

function App() {
    const [data, setData] = useState<string[]>([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000")
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => setData(data["players"]))
            .catch((error) => console.error("Fetch error:", error));
    }, []);

    return (
    <>
        {data.length > 0 ? (
            <ul>
                {data.map((name: string, index: number) => (
                    <li key={index}>{name}</li>
                ))}
            </ul>
        ) : (
            <p>Loading players...</p>
        )}
    </>
     )
}

export default App
