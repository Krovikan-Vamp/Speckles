import pandas as pd, re, os, PyPDF2 as pdf
from time import sleep
from docx import Document
from colorama import Style, Fore
from datetime import date as dt
from docx2pdf import convert

# convert('./medrecs/faxcover.docx')

def docx_replace_regex(doc_obj, regex , replace):
    
    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text

    for table in doc_obj.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_replace_regex(cell, regex , replace)

# print(patient['yourName'])
def main():
    pwChoices = int(input(f'Please select additional docs\nThe fax cover will be made regardless\n1. Anticoagulant\n2. Pacemaker\n3. Both\nSelection: '))
    print(f'You chose: {pwChoices}')
    if (pwChoices == 1):
        docs = [Document('./medrecs/faxcover.docx'), Document('./medrecs/Anticoagulantform.docx'), Document('./medrecs/pacemakerform.docx')]
    elif (pwChoices == 2):
        docs = [Document('./medrecs/faxcover.docx'), Document('./medrecs/pacemakerform.docx')]
    elif (pwChoices == 3):
        docs = [Document('./medrecs/faxcover.docx'), Document('./medrecs/Anticoagulantform.docx'), Document('./medrecs/pacemakerform.docx')]
    else:
        print('Please select a valid option')
        sleep(2)
        print('Restarting...')
        sleep(1)
        main()
        return 1

    patient = {
    "yourName": 'Zackery H./Franchesca G.',
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

    # Input data into tables
    for doc in docs:
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        for word, replacement in patient.items():
                            word_re=re.compile(word)
                            docx_replace_regex(doc, word_re , replacement)
    # Input data into paragraphs
    for doc in docs:
        for word, replacement in patient.items():
            word_re=re.compile(word)
            docx_replace_regex(doc, word_re , replacement)
    # Save the changed files "as"
    x = 0
    for doc in docs:
        if (x == 0):
            doc.save(f"faxcover_{patient['ptName']}.docx")
        elif (x == 1): 
            doc.save(f"anticoag_{patient['ptName']}.docx")
            
        x += 1
        print(x)
    # Edit files to be PDFs
    os.system('powershell docx2pdf .')
    mergeFile = pdf.PdfFileMerger()
    pdfFiles = [pdf.PdfFileReader(f"faxcover_{patient['ptName']}.docx")]
main()