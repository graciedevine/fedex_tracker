import openpyxl

wb = openpyxl.load_workbook("Book5.xlsx")
sheet = wb["Sheet1"]

tracking_number = sheet["B2"].value
