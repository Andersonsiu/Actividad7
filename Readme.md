# Servidor Web Asíncrono con aiohttp

Este proyecto implementa un servidor web asíncrono utilizando `asyncio` y `aiohttp`, ideal para manejar solicitudes HTTP de manera eficiente. El servidor responde con contenido estático y maneja rutas específicas para mostrar el estado del servidor y las tareas en segundo plano.

## Requisitos

Para ejecutar este servidor, necesitas Python 3.7 o superior. Las dependencias del proyecto se pueden instalar utilizando `pip`.

## Estructura del Código

### Variables Globales

-   `start_time`: Registro del momento en que el servidor comenzó a funcionar.
-   `request_count`: Contador de las solicitudes HTTP recibidas por el servidor.
-   `background_tasks_status`: Lista que mantiene el estado de las tareas de fondo ejecutándose.

### Funciones de Manejo de Rutas

-   `handle_home(request)`: Sirve la página de inicio del servidor.
-   `handle_status(request)`: Devuelve un JSON con el estado actual del servidor, incluyendo el tiempo de actividad y el contador de solicitudes.
-   `handle_background_tasks(request)`: Muestra un JSON con el estado actual de las tareas de fondo programadas.

### Middleware

-   `request_count_middleware(request, handler)`: Middleware que incrementa el `request_count` cada vez que se recibe una solicitud.

### Tareas Asíncronas de Fondo

-   `simulate_log_generation()`: Tarea que simula la generación de logs cada 10 segundos.
-   `simulate_maintenance()`: Tarea que simula operaciones de mantenimiento cada 5 minutos.

### Configuración del Servidor y Rutas

El servidor utiliza `aiohttp.web.Application` para configurar y manejar las rutas necesarias para las operaciones del servidor.

### Archivos Estáticos

Los archivos estáticos como HTML, CSS, e imágenes se sirven desde un directorio configurado en las rutas del servidor.

### Funciones de Inicio y Limpieza

-   `start_background_tasks(app)`: Inicia las tareas de fondo al arrancar el servidor.
-   `cleanup_background_tasks(app)`: Limpia y cierra las tareas de fondo al apagar el servidor.
