import ctypes
import os
import subprocess


VERSION = '1.0.2'


def NtMessageType(mtype: str):
    return {'error': 0x10, 'warning': 0x30, 'info': 0x40}.get(mtype, 0)


def CPMessageBox(title: str, body: str, mtype: str):
    if os.name == 'nt': 
        ctypes.WinDLL('user32').MessageBoxW(0, body, title, NtMessageType(mtype))
    else:
        subprocess.run(f"""zenity --{mtype} --title='{title}' --text='{body}'""", shell=True)


def GetMonitorResolution(k: float):
    if os.name == 'nt': 
        return int(ctypes.windll.user32.GetSystemMetrics(0) * k), int(ctypes.windll.user32.GetSystemMetrics(1) * k)
    else: 
        res = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4', 
                                shell=True, 
                                stdout=subprocess.PIPE).communicate()[0].decode().strip().split('x')
        
        return int(res[0]), int(res[1])