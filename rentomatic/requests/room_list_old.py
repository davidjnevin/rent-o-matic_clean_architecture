from collections.abc import Mapping

# This class is used to collect errors for an invalid request
class RoomListInvalidRequest:
    def __init__(self):
        self.errors = []  # List to hold all errors

    # Method to add an error to the errors list
    def add_error(self, parameter, message):
        self.errors.append({"parameter": parameter, "message": message})

    # Method to check if there are any errors
    def has_errors(self):
        return len(self.errors) > 0

    # __bool__ method returns False to indicate this request is not valid
    def __bool__(self):
        return False

# This class is used to hold a valid request
class RoomListValidRequest:
    def __init__(self, filters=None):
        self.filters = filters  # The validated filters

    # __bool__ method returns True to indicate this request is valid
    def __bool__(self):
        return True

# This function is used to validate filters and build the request object
def build_room_list_request(filters=None):
    accepted_filters = ["code__eq", "price__eq", "price__lt", "price__gt"]  # List of valid filter keys
    invalid_req = RoomListInvalidRequest()  # An instance of the invalid request to collect possible errors

    if filters is not None:  # If filters are provided
        if not isinstance(filters, Mapping):  # Check if filters is a mapping (like a dictionary)
            invalid_req.add_error("filters", "Is not iterable")  # If not, add an error
            return invalid_req  # And return the invalid request

        # Check each key in the filters
        for key, value in filters.items():
            if key not in accepted_filters:  # If a key is not in the accepted filters
                invalid_req.add_error(
                    "filters", "Key {} cannot be used".format(key)  # Add an error
                )

        # If any errors were added
        if invalid_req.has_errors():
            return invalid_req  # Return the invalid request

    # If no errors, return a valid request with the filters
    return RoomListValidRequest(filters=filters)

