from pypdf import PdfReader, PdfWriter

merger = PdfWriter()

for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
    reader = PdfReader(pdf, strict=False)  # ignore strict parsing errors
    merger.append(reader)

with open("merged.pdf", "wb") as f_out:
    merger.write(f_out)

