// app/views/DashboardEventsPage.js

import Sidebar from '../components/Sidebar.js';
import ApiService from '../services/ApiService.js';
import { getCurrentUser } from '../utils/Auth.js';

/**
 * Genera el HTML para la página de gestión de eventos del administrador.
 * @param {object} router Instancia del router para la navegación.
 * @returns {string} HTML de la página de dashboard.
 */
const DashboardEventsPage = (router) => {
    const currentUser = getCurrentUser();
    if (!currentUser || currentUser.role !== 'admin') {
        router.navigate('/not-found'); // Redirigir si no es admin
        return 'Redirigiendo...';
    }

    return `
        <div class="dashboard-layout">
            ${Sidebar(router)}
            <div class="main-content">
                <header class="main-header">
                    <h1>Gestión de Eventos</h1>
                    <button id="createEventBtn" class="btn-primary">
                        <i class="fas fa-plus-circle"></i> Crear Nuevo Evento
                    </button>
                </header>
                <section class="events-list-section">
                    <h2>Eventos Registrados</h2>
                    <div id="eventsContainer" class="table-responsive">
                        <p>Cargando eventos...</p>
                    </div>
                    <div id="pagination" class="pagination-controls"></div>
                </section>
            </div>
        </div>
    `;
};

/**
 * Carga y muestra la lista de eventos.
 * @param {object} router Instancia del router.
 */
const loadEvents = async (router) => {
    const eventsContainer = document.getElementById('eventsContainer');
    if (!eventsContainer) return;

    eventsContainer.innerHTML = '<p>Cargando eventos...</p>'; // Mostrar mensaje de carga

    try {
        const events = await ApiService.get('/events'); // Obtener todos los eventos

        if (events.length === 0) {
            eventsContainer.innerHTML = '<p>No hay eventos registrados.</p>';
            return;
        }

        const tableHtml = `
            <table class="data-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Título</th>
                        <th>Fecha</th>
                        <th>Hora</th>
                        <th>Lugar</th>
                        <th>Capacidad</th>
                        <th>Inscritos</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    ${events.map(event => `
                        <tr>
                            <td>${event.id}</td>
                            <td>${event.title}</td>
                            <td>${event.date}</td>
                            <td>${event.time}</td>
                            <td>${event.location}</td>
                            <td>${event.capacity}</td>
                            <td>${event.enrolledUsers ? event.enrolledUsers.length : 0}</td>
                            <td class="actions-cell">
                                <button class="btn-icon btn-edit" data-event-id="${event.id}">
                                    <i class="fas fa-edit"></i>
                                </button>
                                <button class="btn-icon btn-delete" data-event-id="${event.id}">
                                    <i class="fas fa-trash-alt"></i>
                                </button>
                            </td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;
        eventsContainer.innerHTML = tableHtml;

        // Añadir listeners para los botones de editar y eliminar
        document.querySelectorAll('.btn-edit').forEach(button => {
            button.addEventListener('click', () => {
                const eventId = button.dataset.eventId;
                router.navigate(`/dashboard/events/edit/${eventId}`); // Navegar a la página de edición
            });
        });

        document.querySelectorAll('.btn-delete').forEach(button => {
            button.addEventListener('click', async () => {
                const eventId = button.dataset.eventId;
                if (confirm('¿Estás seguro de que quieres eliminar este evento?')) {
                    try {
                        await ApiService.delete(`/events/${eventId}`);
                        alert('Evento eliminado exitosamente.');
                        loadEvents(router); // Recargar la lista de eventos
                    } catch (deleteError) {
                        console.error('Error al eliminar el evento:', deleteError);
                        alert('Error al eliminar el evento.');
                    }
                }
            });
        });

    } catch (error) {
        console.error('Error al cargar los eventos:', error);
        eventsContainer.innerHTML = '<p>Error al cargar los eventos. Inténtalo de nuevo.</p>';
    }
};

/**
 * Agrega los listeners de eventos para la página del dashboard de eventos.
 * @param {object} router Instancia del router para la navegación.
 */
const addDashboardEventsPageListeners = (router) => {
    // Añadir listeners del Sidebar
    Sidebar.addListeners(router);

    // Listener para el botón "Crear Nuevo Evento"
    const createEventBtn = document.getElementById('createEventBtn');
    if (createEventBtn) {
        createEventBtn.addEventListener('click', () => {
            router.navigate('/dashboard/events/create');
        });
    }

    // Cargar los eventos cuando la página esté lista
    loadEvents(router);
};

DashboardEventsPage.addListeners = addDashboardEventsPageListeners;
export default DashboardEventsPage;