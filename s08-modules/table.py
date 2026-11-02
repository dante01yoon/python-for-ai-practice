from rich.console import Console
from rich.table import Table

table = Table(title="Monthly Budget")
table.add_column("Category")
table.add_column("Amount", justify="right")
table.add_row("Rent", "$1,850")
table.add_row("Groceries", "$420")
table.add_row("Gas", "$160")
Console().print(table)
