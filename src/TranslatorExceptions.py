""" Exceptions for the Translator module. """


class ProductException(Exception):
    """Exception raised if there is an issue with product extraction."""

    def __init__(self, message):
        super().__init__(message)


class ForeignNumberException(Exception):
    """Exception raised if there is an issue with foreign number extraction."""

    def __init__(self, message):
        super().__init__(message)
