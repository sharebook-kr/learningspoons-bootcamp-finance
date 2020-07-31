import win32gui

hwnd = win32gui.FindWindow(None, "계산기")
print(hwnd)