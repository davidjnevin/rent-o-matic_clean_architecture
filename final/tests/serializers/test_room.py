# -- coding: utf-8 --
"""

Created on: 11/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import json
import uuid

from rentomatic.serializers.room import RoomJsonEncoder
from rentomatic.domain.room import Room

def test_serializer_domain_room():
    code = uuid.uuid4()

    room = Room(
        code=code,
        size=200,
        price=10,
        longitude=-0.09998975,
        latitude=51.75436293,
    )

    expected_json = f"""
        {{
            "code":"{code}",
            "size": 200,
            "price": 10,
            "longitude": -0.09998975,
            "latitude": 51.75436293
        }}
    """

    json_room = json.dumps(room, cls=RoomJsonEncoder)

    assert json.load(json_room) == json.loads(expected_json)
