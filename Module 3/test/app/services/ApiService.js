// app/services/ApiService.js

const API_BASE_URL = 'http://localhost:3000'; // URL base de tu json-server

class ApiService {
    /**
     * Realiza una petición GET a la API.
     * @param {string} endpoint El endpoint de la API (ej. '/users', '/events').
     * @returns {Promise<Array|Object>} Los datos de la respuesta JSON.
     */
    static async get(endpoint) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`);
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching data:', error);
            throw error;
        }
    }

    /**
     * Realiza una petición POST a la API.
     * @param {string} endpoint El endpoint de la API.
     * @param {object} data Los datos a enviar en el cuerpo de la petición.
     * @returns {Promise<Object>} Los datos de la respuesta JSON.
     */
    static async post(endpoint, data) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error posting data:', error);
            throw error;
        }
    }

    /**
     * Realiza una petición PUT a la API.
     * @param {string} endpoint El endpoint de la API.
     * @param {object} data Los datos a actualizar en el cuerpo de la petición.
     * @returns {Promise<Object>} Los datos de la respuesta JSON.
     */
    static async put(endpoint, data) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error putting data:', error);
            throw error;
        }
    }

    /**
     * Realiza una petición DELETE a la API.
     * @param {string} endpoint El endpoint de la API.
     * @returns {Promise<void>} Una promesa que se resuelve cuando la operación es exitosa.
     */
    static async delete(endpoint) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, {
                method: 'DELETE',
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
            }
            // No hay necesidad de retornar JSON para un DELETE exitoso
        } catch (error) {
            console.error('Error deleting data:', error);
            throw error;
        }
    }
}

export default ApiService;