import openpyxl
book=openpyxl.load_workbook("C:\\Users\\omsri\\Desktop\\Besant  Technologies\\Python\\python_excel.xlsx")
sheet=book.active
cell=sheet.cell(row=4,column=4)
print(cell.value)


sheet['B6']="hello i'm new here"
book.save("C:\\Users\\omsri\\Desktop\\Besant  Technologies\\Python\\python_excel.xlsx")
book.close()