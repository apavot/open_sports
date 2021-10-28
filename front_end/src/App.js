import logo from './logo.svg';
import './App.css';

import { Container } from 'reactstrap';
import NewGameBox from './views/newgamebox';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <NewGameBox />
      </header>
    </div>
  );
}

export default App;
