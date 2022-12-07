from aiohttp import web

from app.context import AppContext
from app import storage, models


async def handle(request: web.Request, context: AppContext) -> web.Response:
    cars = await storage.get_cars(context)
    return web.json_response(
        {'items': [to_response(car) for car in cars]}
    )


def to_response(car: models.Car) -> dict:
    return {
        'id': car.id,
        'location': {'lon': car.location.lon, 'lat': car.location.lat},
        'user': car.user.id if car.user else None
    }
