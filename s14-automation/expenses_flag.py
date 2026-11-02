from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook("expenses.xlsx")
ws = wb["Trip"]
for (cell,) in ws.iter_rows(min_row=2, min_col=3, max_col=3):
    if cell.value > 100:
        cell.font = Font(bold=True, color="C00000")
        print("Over $100:", ws.cell(cell.row, 2).value)

last = ws.max_row
ws.cell(last + 1, 2, "Average")
ws.cell(last + 1, 3, f"=AVERAGE(C2:C{last})").number_format = '"$"#,##0.00'
wb.save("expenses.xlsx")
print("Saved expenses.xlsx")
