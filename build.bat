pyinstaller -w .\code\main.py --hidden-import "pynput.keyboard._win32" --hidden-import "pynput.mouse._win32"