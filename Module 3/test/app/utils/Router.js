// app/utils/Router.js

class Router {
    constructor() {
        this.routes = [];
        this.currentPath = null;
    }

    /**
     * Añade una nueva ruta al enrutador.
     * @param {string} path La ruta (ej. '/login', '/dashboard/events/:id').
     * @param {Function} handler La función a ejecutar cuando la ruta coincide.
     */
    addRoute(path, handler) {
        this.routes.push({ path, handler });
    }

    /**
     * Resuelve la ruta actual, encuentra el manejador correspondiente y lo ejecuta.
     */
    async resolve() {
        this.currentPath = window.location.pathname;
        let matchedRoute = null;

        for (let route of this.routes) {
            const pathSegments = route.path.split('/').filter(s => s.length > 0);
            const currentSegments = this.currentPath.split('/').filter(s => s.length > 0);

            if (pathSegments.length !== currentSegments.length && !route.path.includes(':')) {
                continue;
            }

            let match = true;
            const params = {};

            for (let i = 0; i < pathSegments.length; i++) {
                const pathSegment = pathSegments[i];
                const currentSegment = currentSegments[i];

                if (pathSegment && pathSegment.startsWith(':')) {
                    params[pathSegment.substring(1)] = currentSegment;
                } else if (pathSegment !== currentSegment) {
                    match = false;
                    break;
                }
            }

            if (match) {
                matchedRoute = route;
                await matchedRoute.handler(params);
                return;
            }
        }

        // Si no se encontró ninguna ruta, redirige a /not-found
        this.navigate('/not-found');
    }

    /**
     * Cambia la ruta del navegador y activa la resolución de la ruta.
     * @param {string} path La nueva ruta a navegar.
     */
    navigate(path) {
        window.history.pushState({}, '', path);
        this.resolve();
    }

    /**
     * Inicia el enrutador, resolviendo la ruta inicial y escuchando eventos popstate.
     */
    start() {
        this.resolve();
        // El listener popstate ya está en index.js, así evitamos duplicidad
        // window.addEventListener('popstate', () => this.resolve());
    }
}

export default Router;