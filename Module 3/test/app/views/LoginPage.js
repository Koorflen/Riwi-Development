// app/views/LoginPage.js

import ApiService from '../services/ApiService.js';
import { saveUserToLocalStorage, getCurrentUser } from '../utils/Auth.js';
import Validation from '../utils/Validation.js';
import { renderPage } from '../../index.js';

/**
 * Genera el HTML para la página de inicio de sesión.
 * @returns {string} HTML del formulario de login.
 */
const LoginPage = () => {
    return `
        <div class="auth-container">
            <div class="auth-card">
                <h2>Iniciar Sesión</h2>
                <form id="loginForm">
                    <div class="form-group">
                        <label for="email">Correo electrónico:</label>
                        <input type="email" id="email" name="email" required>
                        <span id="emailError" class="error-message"></span>
                    </div>
                    <div class="form-group">
                        <label for="password">Contraseña:</label>
                        <input type="password" id="password" name="password" required>
                        <span id="passwordError" class="error-message"></span>
                    </div>
                    <button type="submit" class="btn-primary">Iniciar Sesión</button>
                    <p class="mt-3">¿No tienes una cuenta? <a href="/register" id="registerLink">Regístrate aquí</a></p>
                </form>
            </div>
        </div>
    `;
};

/**
 * Agrega los listeners de eventos para la página de inicio de sesión.
 * @param {object} router Instancia del router para la navegación.
 */
const addLoginPageListeners = (router) => {
    const loginForm = document.getElementById('loginForm');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const registerLink = document.getElementById('registerLink');

    // Navegar a registro al hacer clic en el enlace
    if (registerLink) {
        registerLink.addEventListener('click', (e) => {
            e.preventDefault(); // Previene la recarga de la página
            router.navigate('/register');
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault(); // Evita el envío tradicional del formulario

            // Limpiar errores previos
            Validation.clearError('email');
            Validation.clearError('password');

            // Obtener valores
            const email = emailInput ? emailInput.value.trim() : '';
            const password = passwordInput ? passwordInput.value.trim() : '';

            // Validar campos
            let isValid = true;
            let errorMessage = Validation.validateEmail(email);
            if (errorMessage) {
                Validation.displayError('email', errorMessage);
                isValid = false;
            }
            errorMessage = Validation.validateRequired(password);
            if (errorMessage) {
                Validation.displayError('password', errorMessage);
                isValid = false;
            }

            if (!isValid) {
                return; // Detener si hay errores de validación
            }

            try {
                // 1. Verificar si el usuario existe y las credenciales son correctas
                const users = await ApiService.get(`/users?email=${email}&password=${password}`);

                if (users.length > 0) {
                    const user = users[0];
                    saveUserToLocalStorage(user); // Guarda la sesión en localStorage

                    // Redirigir según el rol del usuario
                    if (user.role === 'admin') {
                        router.navigate('/dashboard/events');
                    } else if (user.role === 'visitor') {
                        router.navigate('/visitor/events');
                    }
                } else {
                    // Mostrar error si las credenciales son incorrectas
                    Validation.displayError('password', 'Email o contraseña incorrectos.');
                }
            } catch (error) {
                console.error('Error durante el inicio de sesión:', error);
                // Aquí podrías mostrar un mensaje de error más genérico al usuario
                Validation.displayError('email', 'Error al intentar iniciar sesión. Inténtalo de nuevo.');
            }
        });
    }
};

// Exporta la función de la página y el método para añadir listeners
// Para que el router pueda llamarlo y agregar los listeners después de renderizar.
LoginPage.addListeners = addLoginPageListeners; // Agregamos addListeners como una propiedad estática
export default LoginPage;