import { useEffect, useState } from 'react';
import './App.css'

function App() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch("http://127.0.0.1:8000")
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => setData(data))
            .catch((error) => console.error("Fetch error:", error));
    }, []);

    useEffect(() => {
        console.log(data);
    }, [data]);

    return (
    <>
        <p>
            {data ? JSON.stringify(data, null, 4) : "Loading..."}
        </p>
    </>
     )
}

export default App
