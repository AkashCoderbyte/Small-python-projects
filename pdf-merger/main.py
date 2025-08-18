from PyPDF2 import PdfMerger
merge = PdfMerger()
try:
    n = int(input("tell me the how many number of pdf you like to add : "))
    for i in range (0,n):
        pdf = input(f"give us the name of the of the pdf name {i+1} : ")
        merge.append(pdf)
except Exception as e:
    print("invalid input ")
    exit(1)

merge.write("merged.pdf")
merge.close()

