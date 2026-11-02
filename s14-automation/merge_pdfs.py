from pathlib import Path

from pypdf import PdfReader, PdfWriter

writer = PdfWriter()
for path in sorted(Path("pdfs").glob("*.pdf")):
    writer.append(path)
    print("Added:", path.name)
writer.write("merged.pdf")
print("Total pages:", len(writer.pages))

reader = PdfReader("merged.pdf")
print(reader.pages[2].extract_text())
