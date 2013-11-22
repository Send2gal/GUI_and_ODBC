__author__ = 'Gal'

import xlrd
from datetime import date
from xlwt import Workbook, easyxf
import os
from tempfile import TemporaryFile



filePath = "c:\\Temp\\"
fileName = "my_Excel.xls"

columns = 10
rows    = int(1e1)

def main():
    style1 = easyxf('font: name Times New Roman')
    style2 = easyxf('font: name Times New Roman')
    style3 = easyxf('font: name Times New Roman')

    def write_cells(book):
        sheet = book.add_sheet('Content')
        sheet.write(0,0,'A1',style1)
        sheet.write(0,1,'B1',style2)
        sheet.write(0,2,'C1',style3)

    book = Workbook()
    write_cells(book)
    book.save('3xf3fonts.xls')
    book = Workbook(style_compression=1)
    write_cells(book)
    book.save('3xf1font.xls')
    book = Workbook(style_compression=2)
    write_cells(book)

    #book    = Workbook(encoding = 'Windows-1255')
    #sheet1  = book.add_sheet('sheet 1',cell_overwrite_ok=False)
    #book.add_sheet('sheet 2')
    #sheet1.row(0).hidden = False
    #row_last = sheet1.row(rows)
    #for i in range(columns):
    #    row_last.write(i,'test ' + str(random.randint(1,10)))
    #
    #
    ##Title
    #for col in range(columns):
    #    sheet1.write(0,col,"Colum " +str(col+1),Style.easyxf(''))
    #
    #
    #for row in range(1,rows):
    #    for col in range(columns):
    #        sheet1.write(row,col,str(random.randint(0,1000)))
    #
    #



    book.save(filePath+fileName)
    book.save(TemporaryFile())
    tempString = "excel.exe "+filePath+fileName
    os.system(tempString)


if __name__ == "__main__":
    main()