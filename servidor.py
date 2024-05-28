import asyncio
from aiohttp import web
import json
import datetime

# Variables globales para el estado del servidor
start_time = datetime.datetime.now()
request_count = 0
background_tasks_status = []

# Página de inicio
async def handle_home(request):
    return web.FileResponse('./static/index.html')

# Estado del servidor
async def handle_status(request):
    global request_count
    uptime = datetime.datetime.now() - start_time
    status = {
        "uptime": str(uptime),
        "request_count": request_count
    }
    return web.Response(text=json.dumps(status), content_type='application/json')

# Tareas de fondo
async def handle_background_tasks(request):
    global background_tasks_status
    return web.Response(text=json.dumps(background_tasks_status), content_type='application/json')

# Middleware para contar solicitudes
@web.middleware
async def request_count_middleware(request, handler):
    global request_count
    request_count += 1
    response = await handler(request)
    return response

# Funciones de tareas de fondo
async def simulate_log_generation():
    global background_tasks_status
    while True:
        background_tasks_status.append({"task": "log_generation", "status": "completed"})
        await asyncio.sleep(10)  # Simula la generación de logs cada 10 segundos

async def simulate_maintenance():
    global background_tasks_status
    while True:
        background_tasks_status.append({"task": "maintenance", "status": "completed"})
        await asyncio.sleep(300)  # Simula mantenimiento cada 5 minutos

async def start_background_tasks(app):
    app['log_generation'] = asyncio.create_task(simulate_log_generation())
    app['maintenance'] = asyncio.create_task(simulate_maintenance())

async def cleanup_background_tasks(app):
    app['log_generation'].cancel()
    app['maintenance'].cancel()
    await asyncio.gather(app['log_generation'], app['maintenance'], return_exceptions=True)

# Configuración del servidor y rutas
app = web.Application(middlewares=[request_count_middleware])
app.add_routes([
    web.get('/', handle_home),
    web.get('/status', handle_status),
    web.get('/background-tasks', handle_background_tasks),
])

# Servir archivos estáticos
app.router.add_static('/static', './static')

# Ajustar la configuración del servidor para iniciar y limpiar tareas de fondo
app.on_startup.append(start_background_tasks)
app.on_cleanup.append(cleanup_background_tasks)

# Función principal para iniciar el servidor
def main():
    web.run_app(app, host='127.0.0.1', port=8080)

if __name__ == '__main__':
    main()
