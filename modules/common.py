import ctypes


VERSION = '1.0.1'

MB_ICONERROR: int = 0x10
MB_ICONWARNING: int = 0x30
MB_ICONINFORMATION: int = 0x40


def MessageBox(title: str, body: str, msg_type: int):
    ctypes.WinDLL('user32').MessageBoxW(0, body, title, msg_type)


def GetMonitorResolution(k: float):
    return int(ctypes.windll.user32.GetSystemMetrics(0) * k), int(ctypes.windll.user32.GetSystemMetrics(1) * k)