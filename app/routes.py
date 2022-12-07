from aiohttp import web

from app.api.v1 import get_cars, get_cars_admin
from app.context import AppContext


def wrap_handler(handler, context):
    async def wrapper(request):
        return await handler(request, context)

    return wrapper


def setup_routes(app: web.Application, context: AppContext) -> None:
    app.router.add_get(
        '/v1/cars',
        wrap_handler(get_cars.handle, context)
    )
    app.router.add_get(
        '/v1/admin/cars',
        wrap_handler(get_cars_admin.handle, context)
    )
