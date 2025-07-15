// index.js

import Router from './app/utils/Router.js';
import { getCurrentUser } from './app/utils/Auth.js';
import HomePage from './app/views/HomePage.js';
import LoginPage from './app/views/LoginPage.js';
import RegisterPage from './app/views/RegisterPage.js';
import NotFoundPage from './app/views/NotFoundPage.js';
import DashboardEventsPage from './app/views/DashboardEventsPage.js';
import CreateEventPage from './app/views/CreateEventPage.js';
import EditEventPage from './app/views/EditEventPage.js';
import VisitorEventsPage from './app/views/VisitorEventsPage.js';
import VisitorEnrollmentsPage from './app/views/VisitorEnrollmentsPage.js';


const appRoot = document.getElementById('app');

/**
 * Función para renderizar la página en el contenedor principal de la aplicación.
 * @param {string} content El HTML a inyectar.
 * @param {Function} [addListenersFunction] Función opcional para adjuntar listeners después de renderizar.
 * @param {object} [routerInstance] Instancia del router si es necesaria para los listeners.
 */
export const renderPage = (content, addListenersFunction = null, routerInstance = null) => {
    if (appRoot) {
        appRoot.innerHTML = content;
        if (addListenersFunction && typeof addListenersFunction === 'function') {
            addListenersFunction(routerInstance); // Pasa la instancia del router a los listeners
        }
    }
};

/**
 * Inicializa el enrutador de la aplicación.
 * Define las rutas y sus respectivos manejadores.
 */
const initRouter = () => {
    const router = new Router();

    // Rutas públicas
    router.addRoute('/', async () => {
        const currentUser = getCurrentUser();
        if (currentUser) {
            router.navigate(currentUser.role === 'admin' ? '/dashboard/events' : '/visitor/events');
            return;
        }
        renderPage(HomePage(), HomePage.addListeners, router); // Modificado para pasar listeners
    });
    router.addRoute('/login', async () => {
        if (getCurrentUser()) {
            router.navigate(getCurrentUser().role === 'admin' ? '/dashboard/events' : '/visitor/events');
            return;
        }
        // Aquí, pasamos LoginPage.addListeners y la instancia del router
        renderPage(await LoginPage(), LoginPage.addListeners, router);
    });
    router.addRoute('/register', async () => {
        if (getCurrentUser()) {
            router.navigate(getCurrentUser().role === 'admin' ? '/dashboard/events' : '/visitor/events');
            return;
        }
        // Aquí, pasamos RegisterPage.addListeners y la instancia del router
        renderPage(await RegisterPage(), RegisterPage.addListeners, router);
    });

    // Rutas protegidas para ADMINISTRADOR (ejemplo, se añadirán listeners después)
    router.addRoute('/dashboard/events', async () => {
        const user = getCurrentUser();
        if (!user || user.role !== 'admin') {
            router.navigate('/not-found');
            return;
        }
        renderPage(await DashboardEventsPage(router), DashboardEventsPage.addListeners, router);
    });
    router.addRoute('/dashboard/events/create', async () => {
        const user = getCurrentUser();
        if (!user || user.role !== 'admin') {
            router.navigate('/not-found');
            return;
        }
        renderPage(await CreateEventPage(router), CreateEventPage.addListeners, router); // Asumiendo que CreateEventPage tendrá addListeners
    });
    router.addRoute('/dashboard/events/edit/:id', async (params) => {
        const user = getCurrentUser();
        if (!user || user.role !== 'admin') {
            router.navigate('/not-found');
            return;
        }
        renderPage(await EditEventPage(router, params.id), EditEventPage.addListeners, router); // Asumiendo que EditEventPage tendrá addListeners
    });

    // Rutas protegidas para VISITANTE (ejemplo, se añadirán listeners después)
    router.addRoute('/visitor/events', async () => {
        const user = getCurrentUser();
        if (!user || user.role !== 'visitor') {
            router.navigate('/not-found');
            return;
        }
        renderPage(await VisitorEventsPage(router), VisitorEventsPage.addListeners, router); // Asumiendo que VisitorEventsPage tendrá addListeners
    });
    router.addRoute('/visitor/enrollments', async () => {
        const user = getCurrentUser();
        if (!user || user.role !== 'visitor') {
            router.navigate('/not-found');
            return;
        }
        renderPage(await VisitorEnrollmentsPage(router), VisitorEnrollmentsPage.addListeners, router); // Asumiendo que VisitorEnrollmentsPage tendrá addListeners
    });


    // Ruta para páginas no encontradas o acceso denegado
    router.addRoute('/not-found', () => renderPage(NotFoundPage())); // NotFoundPage no necesita listeners específicos

    // Iniciar el enrutador
    router.start();
};

// Se ejecuta cuando el DOM está completamente cargado
document.addEventListener('DOMContentLoaded', initRouter);

// Manejar cambios en la URL (ej. botones de atrás/adelante del navegador)
window.addEventListener('popstate', initRouter);