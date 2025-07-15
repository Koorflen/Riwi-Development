// app/utils/Auth.js

const USER_STORAGE_KEY = 'currentUser';

/**
 * Guarda la información del usuario en localStorage.
 * @param {object} userData Los datos del usuario a guardar.
 */
export const saveUserToLocalStorage = (userData) => {
    localStorage.setItem(USER_STORAGE_KEY, JSON.stringify(userData));
};

/**
 * Obtiene la información del usuario del localStorage.
 * @returns {object|null} Los datos del usuario o null si no hay sesión.
 */
export const getCurrentUser = () => {
    try {
        const userData = localStorage.getItem(USER_STORAGE_KEY);
        return userData ? JSON.parse(userData) : null;
    } catch (error) {
        console.error("Error parsing user data from localStorage:", error);
        return null;
    }
};

/**
 * Elimina la información del usuario del localStorage, cerrando la sesión.
 */
export const clearUserFromLocalStorage = () => {
    localStorage.removeItem(USER_STORAGE_KEY);
};