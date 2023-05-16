from .common import CPMessageBox


class PaiterException(BaseException):
    def __init__(self, message: str):
        CPMessageBox('010 painter', message, 'error')
        super().__init__()

class NoParamsError(PaiterException):
    def __init__(self):
        super().__init__('No input file specified! Add input file path as an execution param!')

class FileDoentExist(PaiterException):
    def __init__(self, path: str):
        super().__init__("Can't load input file: {}!".format(path))

class InvalidDataFormatError(PaiterException):
    def __init__(self, data: str):
        super().__init__('invalid data format: {}!'.format(data))

class VariableGrapthLenError(PaiterException):
    def __init__(self):
        super().__init__('Grapth data len must be const!')

class MissedPackageError(PaiterException):
    def __init__(self, package: str):
        super().__init__('Missed package: {}!'.format(package))