from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = "Trip"
ws.append(["Date", "Item", "Amount"])
ws.append(["Oct 27", "Flight to Chicago", 248.00])
ws.append(["Oct 27", "Hotel, 2 nights", 389.50])
ws.append(["Oct 28", "Lunch with client", 64.20])
ws.append(["Oct 29", "Taxi to airport", 42.75])
ws["E1"] = "Total"
ws["F1"] = "=SUM(C2:C5)"
for row in ws.iter_rows(min_row=2, min_col=3, max_col=3):
    row[0].number_format = '"$"#,##0.00'
wb.save("expenses.xlsx")

wb2 = load_workbook("expenses.xlsx")
total = 0.0
for date, item, amount in wb2["Trip"].iter_rows(min_row=2, max_col=3, values_only=True):
    print(f"{date}  {item:<20} ${amount:>8.2f}")
    total += amount
print(f"Total: ${total:,.2f}")
