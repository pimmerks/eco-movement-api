class ApiException(Exception):
    """Exception class containing reasons of API get failures.

    Args:
        Exception (_type_): _description_
    """
    def __init__(self, status_message: str, status_code: int):
        self.status_message = status_message
        self.status_code = status_code
