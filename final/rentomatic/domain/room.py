# -- coding: utf-8 --
"""

Created on: 9/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import uuid
import dataclasses

@dataclasses.dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)



