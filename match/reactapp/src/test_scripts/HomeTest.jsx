import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import HomePage from "./HomePage";
import ProjectPage from "./ProjectPage";
import { AuthProvider } from './AuthContext';

function App() {
  return (

    <div className="app__body">
      <HomePage />
    </div>
  );
}

export default App;