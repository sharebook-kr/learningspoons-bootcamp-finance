import win32com.client

ie = win32com.client.Dispatch("InternetExplorer.Application")
ie.Visible = True
