import json  # Import the json module from the Python standard library


# Define a new class RoomJsonEncoder, subclassing from json.JSONEncoder
class RoomJsonEncoder(json.JSONEncoder):
    # Override the default method of JSONEncoder
    def default(self, o):
        # Try to serialize the object
        try:
            # Assume that o is a Room object and extract its attributes.
            # Each attribute is transformed to a serializable type (for instance, o.code is transformed to a string).
            # All attributes are gathered in a dictionary.
            to_serialize = {
                "code": str(o.code),  # 'o.code' is converted to a string
                "size": o.size,  # 'o.size' is directly used, it should be a JSON serializable type
                "price": o.price,  # 'o.price' is directly used, it should be a JSON serializable type
                "latitude": o.latitude,  # 'o.latitude' is directly used, it should be a JSON serializable type
                "longitude": o.longitude,  # 'o.longitude' is directly used, it should be a JSON serializable type
            }
            return to_serialize  # The dictionary is returned. This dictionary will be serialized to JSON.
        except AttributeError:  # pragma: no cover
            # If an AttributeError is raised (this happens if o is not a Room object, or if an attribute is missing),
            # then fallback on the default serialization method.
            return super().default(o)  # Call the 'default' method from the parent class 'json.JSONEncoder'
