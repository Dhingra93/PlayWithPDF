import fitz
import pandas as pd
import tabula

"""
Libraries to install using pip install
PyMUPDF =>To read PDF
FPFF=> Create PDF 
"""

def readPDFContent():
    content=""
    with fitz.open('students.pdf') as pdf:
        for page in pdf:
            content+=page.get_text()
        print(content)


def readTablesFromPDF():
    table=tabula.read_pdf('weather.pdf',pages='all')  # this will return the datatables avaialble in formated pdf
    #pages can be 1 ,2 or all
    df=table[0]
    df.to_csv('WeatherInCSV.csv',index=None)


def PDFtoExcel():
    table=tabula.read_pdf('Table+and+Text.pdf',pages=1)
    df=table[0]

    with pd.ExcelWriter("Table1.xlsx") as writer:
        df.to_excel(writer,index=False)

