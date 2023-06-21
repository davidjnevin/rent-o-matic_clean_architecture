# -- coding: utf-8 --
"""

Created on: 11/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import json
from typing import Any


class RoomJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        try:
            to_serializer = {
                "code": str(o.code),
                "size": o.size,
                "price": o.price,
                "latitude": o.latitude,
                "longitudw": o.longitude,
            }
            return to_serializer
        except AttributeError: # pragma: no cover
            return super().default(o)
