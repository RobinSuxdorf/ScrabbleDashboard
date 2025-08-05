import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import GameList from './game-list';
import GameView from './game-view';


function App() {
    return (
        <BrowserRouter>
            <Routes>
                    <Route path="games" element={<GameList />} />
                    <Route path="games/:id" element={<GameView />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
