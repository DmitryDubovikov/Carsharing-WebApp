import typing as tp
from app.context import AppContext
from app import models


async def get_cars(context: AppContext) -> tp.List[models.Car]:
    # query = '''
    # select id, location, user from cars
    # '''
    #
    # rows = await context.db.fetch(query)
    # TODO
    rows = [{'id': 111, 'location': [55.607847, 37.579487], 'user': 555}]

    return [models.Car.from_db(row) for row in rows]

