import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './main.css';
import './index.css';
import App from './App.js';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
);