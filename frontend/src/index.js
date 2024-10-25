import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';  // You can include global styles if needed
import App from './App';  // Import the root component
import reportWebVitals from './reportWebVitals';  // Optional for performance measuring

// Render the App component into the 'root' div in public/index.html
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (e.g., reportWebVitals(console.log)) or send to an analytics endpoint.
reportWebVitals();
