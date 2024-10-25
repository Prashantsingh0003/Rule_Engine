import React from 'react';
import './App.css';  // Import the CSS file for styling
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CreateRule from './components/CreateRule';
import CombineRules from './components/CombineRules';
import EvaluateRule from './components/EvaluateRule';

function App() {
  return (
    <Router>
      <div className="App">
        <div className="navbar">
          <Link to="/">Home</Link>
          <Link to="/create">Create Rule</Link>
          <Link to="/combine">Combine Rules</Link>
          <Link to="/evaluate">Evaluate Rule</Link>
        </div>

        <div className="container">
          <h1>Rule Engine with AST</h1>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/create" element={<CreateRule />} />
            <Route path="/combine" element={<CombineRules />} />
            <Route path="/evaluate" element={<EvaluateRule />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

// Home component for the default route
function Home() {
  return <h2>Welcome to the Rule Engine</h2>;
}

export default App;
