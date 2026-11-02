from pathlib import Path
from string import Template

letter = Template("Hi $name,\nyour order of $item ships on $day.\nThanks, Dante\n")
Path("letters").mkdir(exist_ok=True)
for name, item, day in [("Maya", "a desk lamp", "Monday"), ("Leo", "two mugs", "Tuesday")]:
    Path("letters", f"{name}.txt").write_text(letter.substitute(name=name, item=item, day=day))
    print("Wrote", name)
