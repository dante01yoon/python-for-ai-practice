# Scope: variables made inside a function stay inside
total = 0

def add_tip(bill):
    tip = bill * 0.2
    return bill + tip

total = add_tip(50)
print(total)
print(tip)
