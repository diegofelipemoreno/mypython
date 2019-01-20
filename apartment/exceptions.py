class InputException(Exception):
    def __init__(self, type_input):
        super().__init__(type_input)
        self.type_input = type_input

class InvalidTypeValue(InputException):
    pass
