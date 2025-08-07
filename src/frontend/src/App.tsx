import './App.css';
import { BrowserRouter, Link, Routes, Route } from 'react-router-dom';
import GameList from './game-list';
import GameView from './game-view';
import PlayerList from './player-list';
import PlayerView from './player-view';
import { AppBar, Button, Toolbar, Typography } from '@mui/material';


function App() {
    return (
        <BrowserRouter>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6">
                        Scrabble Dashboard
                    </Typography>
                    <Button color="inherit" component={Link} to="/games/">
                        Games
                    </Button>
                    <Button color="inherit" component={Link} to="/players/">
                        Players
                    </Button>
                </Toolbar>
            </AppBar>
            <Routes>
                <Route path="games" element={<GameList />} />
                <Route path="games/:id" element={<GameView />} />
                <Route path="players" element={<PlayerList />} />
                <Route path="players/:id" element={<PlayerView />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
