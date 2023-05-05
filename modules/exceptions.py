from .common import MessageBox, MB_ICONERROR


class PaiterException(BaseException):
    def __init__(self, message: str):
        MessageBox('Error', message, MB_ICONERROR)
        super().__init__()

class NoParamsError(PaiterException):
    def __init__(self):
        super().__init__('No input file specified! Add input file path as an execution param!')

class FileDoentExist(PaiterException):
    def __init__(self, path: str):
        super().__init__("Can't load input file:\n" + path)

class InvalidDataFormatError(PaiterException):
    def __init__(self, data: str):
        super().__init__('invalid data format:\n' + data)

class VariableGrapthLenError(PaiterException):
    def __init__(self):
        super().__init__('Grapth data len must be const!')