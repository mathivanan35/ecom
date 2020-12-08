import openpyxl

def read(i, j):
    sheet_location = r"C:\Users\GT Sanatorium\PycharmProjects\Flipkart\data_sheet\Data.xlsx"
    book = openpyxl.load_workbook(sheet_location)
    active_sheet = book.active
    cell = active_sheet.cell(i, j)
    value = cell.value
    return value