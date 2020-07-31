import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Range("A1:A10").Value = "hello"
ws.Cells(2,2).Value = 3

for i in range(1, 10):
    ws.Cells(i, 3).Value = "world"

