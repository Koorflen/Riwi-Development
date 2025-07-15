// app/views/HomePage.js

import { renderPage } from '../../index.js'; // Importa la función renderPage de index.js
import LoginPage from './LoginPage.js';
import RegisterPage from './RegisterPage.js';

/**
 * Genera el HTML para la página de inicio.
 * @returns {string} HTML de la página de inicio.
 */
const HomePage = () => {
    // Retorna una plantilla de string con el HTML de la página de bienvenida
    return `
        <div class="welcome-container">
            <div class="welcome-card">
                <h1>Bienvenido</h1>
                <div class="welcome-buttons">
                    <button id="registerBtn" class="btn-primary">Registrarse</button>
                    <button id="loginBtn" class="btn-secondary">Iniciar Sesión</button>
                </div>
            </div>
        </div>
    `;
};

/**
 * Agrega los listeners de eventos para la página de inicio.
 * Se llama después de que el HTML de la página se ha renderizado.
 */
const addHomePageListeners = (router) => {
    const registerBtn = document.getElementById('registerBtn');
    const loginBtn = document.getElementById('loginBtn');

    if (registerBtn) {
        registerBtn.addEventListener('click', () => {
            router.navigate('/register'); // Usar router.navigate
        });
    }

    if (loginBtn) {
        loginBtn.addEventListener('click', () => {
            router.navigate('/login'); // Usar router.navigate
        });
    }
};

HomePage.addListeners = addHomePageListeners;
export default HomePage;
// Se debe llamar a addHomePageListeners después de renderizar HomePage en index.js
// o en el router. Sin embargo, para simplificar por ahora, la vamos a exportar
// y llamar manualmente o el router mismo gestionará la inyección de eventos.
// Para esta estructura, el Router llama a renderPage, así que los listeners
// deben ser manejados por el Router o por cada vista cuando se carga.

// Una mejor práctica sería que cada vista gestione sus propios listeners
// después de ser inyectada en el DOM. Lo haremos en los siguientes pasos.
// Por ahora, solo exportamos el HTML.