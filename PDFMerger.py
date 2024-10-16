'''WAP to manipulate pdf files using pyPDF . 
Your pograms should be able to merge multiple pdf files into a single pdf file.
You are welcome to add more functionalities'''

'''pyPDF is a free and open-source pure-python PDF library capable of splitting,merging,cropping and transforming
the pages of PDF files.
It can also add custom data,viewing options and passwords to PDF files.
pyPDF can retrieve text and metadata from PDFs as well'''

from pypdf import PdfWriter
merger=PdfWriter()

for pdf in ["Apna College notes.pdf","Python Crash Course.pdf","Python_Complete_Notes.pdf"]:
    merger.append(pdf)
merger.write("Merged_Python_Notes.pdf")
merger.close()