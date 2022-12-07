import typing as tp
from app.context import AppContext
from app import models
import sqlite3


async def get_cars(context: AppContext) -> tp.List[models.Car]:
    query = '''
    select id, lat, lon, user from cars
    '''

    con = sqlite3.connect("cars.sqlite3")
    cur = con.cursor()
    rows = cur.execute(query)

    # rows = [{'id': 111, 'location': [55.607847, 37.579487], 'user': 555}]

    return [models.Car.from_db(row) for row in rows]

