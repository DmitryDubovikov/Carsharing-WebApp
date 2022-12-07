from __future__ import annotations
import typing as tp

import dataclasses


@dataclasses.dataclass
class User:
    id: str

    @classmethod
    def from_db(cls, user_id: tp.Optional[str]) -> User:
        if user_id:
            return User(id=user_id)
        else:
            return None


@dataclasses.dataclass
class Location:
    lat: float
    lon: float


@dataclasses.dataclass
class Car:
    id: str
    location: Location
    user: tp.Optional[User] = None

    @classmethod
    def from_db(cls, row) -> Car:
        print(row)
        return cls(
            id=row[0],
            location=Location(lat=row[1], lon=row[2]),
            user=User.from_db(row[3])
        )

