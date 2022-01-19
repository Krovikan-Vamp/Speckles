import time, os, pickle, shutil, pyautogui as pag
import PyPDF2 as pdf
from datetime import date as dt
from colorama import Style, Fore


# input(f"{Fore.RED}YOU NEED TO OPEN 'faxcover.docx' FOR THIS TO WORK{Style.RESET_ALL}\n{Fore.YELLOW}DOUBLE CHECK SELECTED DOCUMENTS{Style.RESET_ALL}")
userprof = os.environ['USERPROFILE']
print(userprof)
# Collect the patient/fax information in one spot, one time
patient = {
    "yourName" : 'Zackery H./Franchesca G.',
    "dateOfFax": dt.today().strftime("%B %d, %Y"),
    "urgency": 'URGENT',
    "numberOfPages": input(f'How many {Fore.YELLOW}pages{Style.RESET_ALL} are being faxed?\n'),
    "fNumber": input(f'What is the number you are {Fore.RED}faxing to{Style.RESET_ALL}?\n'),
    "pNumber": input(f'What is the {Fore.RED}phone number{Style.RESET_ALL} of the facility you are faxing?\n'),
    "drName": input(f'What is the name of the {Fore.RED}doctor you are contacting{Style.RESET_ALL}? (Name only! No "Dr." needed!)\n'),
    "ptName": input(f'What is the name of the {Fore.RED}patient{Style.RESET_ALL}?\n'),
    "dateOfBirth": input(f"What is the patient's {Fore.RED}date of birth{Style.RESET_ALL}?\n"),
    "procedureName": input(f'What is the {Fore.RED}procedure name{Style.RESET_ALL}? (i.e. PVP (Photovaporization of the prostate))\n'),
    "procedureDate": input(f'What is the {Fore.RED}date{Style.RESET_ALL} of the procedure?\n'),
    "anesthesiologistName": input(f'Who is the {Fore.RED}surgeon{Style.RESET_ALL}? (Kaplan, Wong...)\n')
}

# Moving around with pyautogui
def find(key):
    time.sleep(0.5)
    pag.hotkey('ctrl', 'f')
    time.sleep(0.5)
    pag.hotkey('ctrl', 'f')
    time.sleep(0.5)
    pag.write(key)
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(0.5)
    pag.press('esc')
    time.sleep(0.5)

def savePDF(func, pt):
    time.sleep(1)
    os.system(f'mkdir "{userprof}/Desktop/Medical Records PDFs"')
    time.sleep(1)
    pag.press('f12')
    time.sleep(1)
    pag.write(f"{func}_{pt['ptName']}.pdf")
    pag.press('tab')
    pag.write('pdf')
    pag.hotkey('ctrl', 'l')
    pag.write(f'{userprof}/Desktop/Medical Records PDFs')
    pag.press('enter', 5, 0.5)
    time.sleep(2)
    pag.hotkey('crtl', 'w')

def mergePDFs(pt):
    
    ogFilesPaths = [f'{userprof}/Desktop/Medical Records PDFs/faxcover_{pt["ptName"]}.pdf', f'{userprof}/Desktop/Medical Records PDFs/anticoag_{pt["ptName"]}.pdf', f'{userprof}/Desktop/Medical Records PDFs/pacemaker_{pt["ptName"]}.pdf']
    for path in ogFilesPaths:
        shutil.move(path, './')
    os.system('cd {userprof}/Desktop/Medical Records PDFs')
    os.system('move *.pdf "{userprof}/Desktop/Python"')
    time.sleep(1)
    mergeFile = pdf.PdfFileMerger()
    pdfFiles = [pdf.PdfFileReader(f'faxcover_{pt["ptName"]}.pdf', 'rb'), pdf.PdfFileReader(f'anticoag_{pt["ptName"]}.pdf', 'rb'), pdf.PdfFileReader(f'pacemaker_{pt["ptName"]}.pdf', 'rb')]
    for file in pdfFiles:
        mergeFile.append(file)
    names = pt['ptName'].split(' ')
    mergeFile.write(f'Request- {names[1]}, {names[0]} med recs req.pdf')


# Fill out the fax cover
def Fax_Cover():
    os.system(r"powershell medrecs\\faxcover.docx") # Fax Cover sheet
    time.sleep(3) # Wait for Word  to load
    os.system(r"powershell medrecs\\faxcover.docx")
    for key, value in patient.items(): # For each key needed for the cover, find it in document and replace with value
        find(key)
        pag.write(value)
    savePDF('faxcover', patient)
    print(f"Just finished the {Fore.GREEN}Fax Cover{Style.RESET_ALL}, you should probably {Fore.MAGENTA}print{Style.RESET_ALL} it.")

# Fill out the anticoag form if needed
def Anticoag_Form():
    anticoag_params = ['drName', 'pNumber', 'fNumber', 'dateOfFax', 'procedureName', 'ptName', 'dateOfBirth', 'procedureDate']
    os.system(r"powershell medrecs\\Anticoagulantform.docx") # Anticoag Form
    time.sleep(3)
    os.system(r"powershell medrecs\\Anticoagulantform.docx")

    for param in anticoag_params: # Loop through params and fill needed values
        find(param)
        pag.write(patient[param])
    savePDF('anticoag', patient)
    print(f"Just finished the {Fore.GREEN}Anticoagulant form{Style.RESET_ALL}, you should probably {Fore.MAGENTA}print{Style.RESET_ALL} it.")

# Fill out the pacemaker form if needed
def Pacemaker_Form():
    pacemaker_params = ['ptName', 'dateOfBirth', 'procedureName', 'procedureDate', 'drName']
    os.system(r"powershell medrecs\\pacemakerform.docx") # Pacemaker info sheet
    time.sleep(5)
    os.system(r"powershell medrecs\\pacemakerform.docx")

    for param in pacemaker_params: # Loop through params and fill needed values
        find(param)
        pag.write(patient[param])
    savePDF('pacemaker', patient)
    print(f"Just finished the {Fore.GREEN}Pacemaker form{Style.RESET_ALL}, you should probably {Fore.MAGENTA}print{Style.RESET_ALL} it.")

Fax_Cover()
Anticoag_Form()
Pacemaker_Form()
mergePDFs(patient)

