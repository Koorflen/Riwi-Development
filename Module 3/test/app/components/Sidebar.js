// app/components/Sidebar.js

import { getCurrentUser, clearUserFromLocalStorage } from '../utils/Auth.js';

/**
 * Genera el HTML para la barra lateral de navegación.
 * Los enlaces cambian según el rol del usuario (admin o visitor).
 * @param {object} router Instancia del router para la navegación.
 * @returns {string} HTML de la barra lateral.
 */
const Sidebar = (router) => {
    const currentUser = getCurrentUser();
    console.log('Current User in Sidebar:', currentUser);
    if (!currentUser) {
        return ''; // No renderizar sidebar si no hay usuario logueado
    }

    let linksHtml = '';
    let logoutButton = `
        <button id="logoutBtn" class="sidebar-button sidebar-logout">
            <i class="fas fa-sign-out-alt"></i> Cerrar Sesión
        </button>
    `;

    if (currentUser.role === 'admin') {
        linksHtml = `
            <a href="/dashboard/events" class="sidebar-link" data-path="/dashboard/events">
                <i class="fas fa-calendar-alt"></i> Gestión de Eventos
            </a>
            <a href="/dashboard/events/create" class="sidebar-link" data-path="/dashboard/events/create">
                <i class="fas fa-plus-circle"></i> Crear Evento
            </a>
            `;
    } else if (currentUser.role === 'visitor') {
        linksHtml = `
            <a href="/visitor/events" class="sidebar-link" data-path="/visitor/events">
                <i class="fas fa-calendar-check"></i> Eventos Disponibles
            </a>
            <a href="/visitor/enrollments" class="sidebar-link" data-path="/visitor/enrollments">
                <i class="fas fa-user-check"></i> Mis Inscripciones
            </a>
            `;
    }

    return `
        <div class="sidebar">
            <div class="sidebar-header">
                <h3>Event Manager</h3>
                <p>Bienvenido, ${currentUser.fullName}</p>
                <p class="user-role">(${currentUser.role === 'admin' ? 'Administrador' : 'Visitante'})</p>
            </div>
            <nav class="sidebar-nav">
                ${linksHtml}
            </nav>
            ${logoutButton}
        </div>
    `;
};

/**
 * Agrega los listeners de eventos a la barra lateral.
 * @param {object} router Instancia del router para la navegación.
 */
const addSidebarListeners = (router) => {
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            clearUserFromLocalStorage(); // Limpia la sesión del localStorage
            router.navigate('/'); // Redirige a la página de inicio
        });
    }

    // Manejar clics en los enlaces de la barra lateral
    const sidebarLinks = document.querySelectorAll('.sidebar-link');
    sidebarLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const path = link.getAttribute('data-path');
            if (path) {
                router.navigate(path);
            }
        });
    });
};

Sidebar.addListeners = addSidebarListeners; // Adjuntar la función de listeners
export default Sidebar;