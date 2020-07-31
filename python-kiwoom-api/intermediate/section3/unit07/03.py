import win32gui
import win32con
import win32api

hwnd = win32gui.FindWindow(None, "*제목 없음 - Windows 메모장")
edit = win32gui.GetDlgItem(hwnd, 0xF)

win32api.SendMessage(edit, win32con.WM_CHAR, ord('H'), 0)
win32api.Sleep(100)    # 0.1
win32api.SendMessage(edit, win32con.WM_CHAR, ord('i'), 0)
win32api.Sleep(100)    # 0.1


