# import xlsxwriter module
import xlsxwriter, os, openpyxl as oxl

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
os.system('cls')
workbook = xlsxwriter.Workbook('hello.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()
# workbook.close()
# Use the worksheet object to write
# data via the write() method.
headers = ['Patient Name,' 	'DOB', 	'DOS', 	'Procedure', 	'Physician', 	'PCP',	'ph/fax',	'Cardio',	'ph/fax2',
           'A1c',	'Pacemaker',	'EKG', 	'Med Recs',	'Clearance',	'AntiCoag',	'Date Faxed', 	'Date Received', 	'Notes']

# Write headers if not existing in the sheet
fn = 'hello.xlsx'
wb = oxl.load_workbook(fn)
ws = wb.active
if ws.max_row == 1:
    for header in headers:
        worksheet.write(0, headers.index(header), header)
    print('Added headers...')

# Finally, close the Excel file
# via the close() method.
wb.save(fn)
workbook.close()
