__author__ = 'Gal'
import xlrd

filePath = "c:\\Temp\\"
fileName = "exsel.xlsx"


def printAllSheetCellByCell(mySheet):
     #see all the cel [Address of the cell -- Cell contents] , Example : B2 - abcd
     for row_index in range(mySheet.nrows):
         for col_index in range(mySheet.ncols):
             print xlrd.cellname(row_index,col_index),'-',mySheet.cell(row_index,col_index).value


def main():
     wb     = xlrd.open_workbook(filePath+fileName)
     sheet  = wb.sheet_by_index(0)
     #printAllSheetCellByCell(sheet)











if __name__ == "__main__":
    main()