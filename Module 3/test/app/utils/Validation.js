// app/utils/Validation.js

class Validation {
    /**
     * Valida que un campo no esté vacío.
     * @param {string} value El valor del campo.
     * @returns {string|null} Mensaje de error si está vacío, null si es válido.
     */
    static validateRequired(value) {
        return value && value.trim() !== '' ? null : 'Este campo es obligatorio.';
    }

    /**
     * Valida un formato de email básico.
     * @param {string} email El email a validar.
     * @returns {string|null} Mensaje de error si el formato es inválido, null si es válido.
     */
    static validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email) ? null : 'Introduce un formato de email válido.';
    }

    /**
     * Valida que una contraseña tenga al menos 6 caracteres.
     * @param {string} password La contraseña a validar.
     * @returns {string|null} Mensaje de error si es muy corta, null si es válida.
     */
    static validatePassword(password) {
        return password.length >= 6 ? null : 'La contraseña debe tener al menos 6 caracteres.';
    }

    /**
     * Valida que dos contraseñas coincidan.
     * @param {string} password La primera contraseña.
     * @param {string} confirmPassword La segunda contraseña para confirmar.
     * @returns {string|null} Mensaje de error si no coinciden, null si coinciden.
     */
    static validatePasswordMatch(password, confirmPassword) {
        return password === confirmPassword ? null : 'Las contraseñas no coinciden.';
    }

    /**
     * Valida la longitud mínima de un campo.
     * @param {string} value El valor del campo.
     * @param {number} minLength La longitud mínima requerida.
     * @param {string} fieldName El nombre del campo para el mensaje de error.
     * @returns {string|null} Mensaje de error si es muy corto, null si es válido.
     */
    static validateMinLength(value, minLength, fieldName = 'Este campo') {
        return value.length >= minLength ? null : `${fieldName} debe tener al menos ${minLength} caracteres.`;
    }

    /**
     * Limpia un mensaje de error visual para un campo.
     * @param {string} fieldId El ID del campo (ej. 'email', 'password').
     */
    static clearError(fieldId) {
        const errorElement = document.getElementById(`${fieldId}Error`);
        if (errorElement) {
            errorElement.textContent = '';
            errorElement.style.display = 'none';
        }
        const inputElement = document.getElementById(fieldId);
        if (inputElement) {
            inputElement.classList.remove('input-error');
        }
    }

    /**
     * Muestra un mensaje de error visual para un campo.
     * @param {string} fieldId El ID del campo.
     * @param {string} message El mensaje de error a mostrar.
     */
    static displayError(fieldId, message) {
        const errorElement = document.getElementById(`${fieldId}Error`);
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.style.display = 'block';
        }
        const inputElement = document.getElementById(fieldId);
        if (inputElement) {
            inputElement.classList.add('input-error');
        }
    }
}

export default Validation;