import openpyxl
wb = openpyxl.Workbook() # Create a new workbook
sheet = wb.sheetnames # Get the sheet names as a List
print(sheet) # Prints ['Sheet']
sheet1 = wb["Sheet"] # Get the first sheet
sheet1['A1'].value = 163 # Set the value of cell A1 to 42
sheet1['A2'].value = 164 # Set the value of cell A1 to 42
sheet1['A3'].value = 165 # Set the value of cell A1 to 42
sheet1['B1'].value = 'Subramanya' # Set the value of cell A1 to 42
sheet1['B2'].value = 'Sudhanva' # Set the value of cell A1 to 42
sheet1['B3'].value = 'Sujay' # Set the value of cell A1 to 42

wb.save('example2.xlsx') # Save the workbook to a file
