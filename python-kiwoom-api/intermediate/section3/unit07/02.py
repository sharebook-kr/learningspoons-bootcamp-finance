import win32gui
import win32con

hwnd = win32gui.FindWindow(None, "계산기")
win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

