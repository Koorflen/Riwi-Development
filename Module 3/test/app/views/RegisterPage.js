// app/views/RegisterPage.js

import ApiService from '../services/ApiService.js';
import { saveUserToLocalStorage } from '../utils/Auth.js';
import Validation from '../utils/Validation.js';
import { renderPage } from '../../index.js'; // Necesario para la redirección después del registro

/**
 * Genera el HTML para la página de registro.
 * @returns {string} HTML del formulario de registro.
 */
const RegisterPage = () => {
    return `
        <div class="auth-container">
            <div class="auth-card">
                <h2>Registrarse</h2>
                <form id="registerForm">
                    <div class="form-group">
                        <label for="fullName">Nombre Completo:</label>
                        <input type="text" id="fullName" name="fullName" required>
                        <span id="fullNameError" class="error-message"></span>
                    </div>
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
                    <div class="form-group">
                        <label for="confirmPassword">Confirmar Contraseña:</label>
                        <input type="password" id="confirmPassword" name="confirmPassword" required>
                        <span id="confirmPasswordError" class="error-message"></span>
                    </div>
                    <button type="submit" class="btn-primary">Registrarse</button>
                    <p class="mt-3">¿Ya tienes una cuenta? <a href="/login" id="loginLink">Inicia sesión aquí</a></p>
                </form>
            </div>
        </div>
    `;
};

/**
 * Agrega los listeners de eventos para la página de registro.
 * @param {object} router Instancia del router para la navegación.
 */
const addRegisterPageListeners = (router) => {
    const registerForm = document.getElementById('registerForm');
    const fullNameInput = document.getElementById('fullName');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const loginLink = document.getElementById('loginLink');

    // Navegar a login al hacer clic en el enlace
    if (loginLink) {
        loginLink.addEventListener('click', (e) => {
            e.preventDefault(); // Previene la recarga de la página
            router.navigate('/login');
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault(); // Evita el envío tradicional del formulario

            // Limpiar errores previos
            Validation.clearError('fullName');
            Validation.clearError('email');
            Validation.clearError('password');
            Validation.clearError('confirmPassword');

            // Obtener valores
            const fullName = fullNameInput ? fullNameInput.value.trim() : '';
            const email = emailInput ? emailInput.value.trim() : '';
            const password = passwordInput ? passwordInput.value.trim() : '';
            const confirmPassword = confirmPasswordInput ? confirmPasswordInput.value.trim() : '';

            // Validar campos
            let isValid = true;
            let errorMessage;

            errorMessage = Validation.validateRequired(fullName);
            if (errorMessage) { Validation.displayError('fullName', errorMessage); isValid = false; }

            errorMessage = Validation.validateEmail(email);
            if (errorMessage) { Validation.displayError('email', errorMessage); isValid = false; }
            
            errorMessage = Validation.validatePassword(password);
            if (errorMessage) { Validation.displayError('password', errorMessage); isValid = false; }

            errorMessage = Validation.validatePasswordMatch(password, confirmPassword);
            if (errorMessage) { Validation.displayError('confirmPassword', errorMessage); isValid = false; }


            if (!isValid) {
                return; // Detener si hay errores de validación
            }

            try {
                // 1. Verificar si el email ya está registrado
                const existingUsers = await ApiService.get(`/users?email=${email}`);
                if (existingUsers.length > 0) {
                    Validation.displayError('email', 'Este email ya está registrado.');
                    return;
                }

                // 2. Registrar nuevo usuario como 'visitor' por defecto
                const newUser = {
                    fullName,
                    email,
                    password, // En una app real, la contraseña sería hasheada antes de guardar
                    role: 'visitor' // Rol por defecto para nuevos registros
                };

                const registeredUser = await ApiService.post('/users', newUser);
                saveUserToLocalStorage(registeredUser); // Guarda la sesión del nuevo usuario

                // Redirigir al dashboard de visitante
                router.navigate('/visitor/events');

            } catch (error) {
                console.error('Error durante el registro:', error);
                Validation.displayError('email', 'Error al intentar registrar el usuario. Inténtalo de nuevo.');
            }
        });
    }
};

// Adjunta addListeners como una propiedad estática de RegisterPage
RegisterPage.addListeners = addRegisterPageListeners;
export default RegisterPage;