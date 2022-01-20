from code import interact
from importlib.metadata import files
import re, os
from time import sleep
from docx import Document
from datetime import date as dt
from phaxio import PhaxioApi

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
    import PyPDF2 as pdf    
    pwChoices = int(input(f'Please select additional docs\nThe fax cover will be made regardless\n1. Both                  2. Pacemaker\n3. Anticoagulant         4. Faxcover only\nSelection: '))
    print(f'You chose: {pwChoices}')
    if (pwChoices == 1):
        docs = [Document('./medrecs/faxcover.docx'), Document('./medrecs/Anticoagulantform.docx'), Document('./medrecs/pacemakerform.docx')]
    elif (pwChoices == 2):
        docs = [Document('./medrecs/faxcover.docx'), Document('./medrecs/pacemakerform.docx')]
    elif (pwChoices == 3):
        docs = [Document('./medrecs/faxcover.docx'), Document('./medrecs/Anticoagulantform.docx')]
    elif (pwChoices == 4):
        docs = [Document('./medrecs/faxcover.docx')]
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
    "numberOfPages": input(f'How many pages are being faxed?\n'),
    "fNumber": input(f'What is the number you are faxing to?\n'),
    "pNumber": input(f'What is the phone number of the facility you are faxing?\n'),
    "drName": input(f'What is the name of the doctor you are contacting? (Name only! No "Dr." needed!)\n'),
    "ptName": input(f'What is the name of the patient?\n'),
    "dateOfBirth": input(f"What is the patient's date of birth?\n"),
    "procedureName": input(f'What is the procedure name? (i.e. PVP (Photovaporization of the prostate))\n'),
    "procedureDate": input(f'What is the date of the procedure?\n'),
    "anesthesiologistName": input(f'Who is the surgeon? (Kaplan, Wong...)\n')
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
        elif (x == 1 and pwChoices == 2): 
            doc.save(f"pacemaker_{patient['ptName']}.docx")
        elif (x == 1 and pwChoices != 2):
            doc.save(f"anticoag_{patient['ptName']}.docx")
        elif (x == 2 and pwChoices == 1):
            doc.save(f"pacemaker_{patient['ptName']}.docx")
        x += 1
    # Edit files to be PDFs
    os.system('powershell docx2pdf .')
    sleep(2)
    mergeFile = pdf.PdfFileMerger()
    if (pwChoices == 1):
        pdfFiles = [pdf.PdfFileReader(f'faxcover_{patient["ptName"]}.pdf', 'rb'), pdf.PdfFileReader(f'anticoag_{patient["ptName"]}.pdf', 'rb'), pdf.PdfFileReader(f'pacemaker_{patient["ptName"]}.pdf', 'rb')]
    elif (pwChoices == 2):
        pdfFiles = [pdf.PdfFileReader(f'faxcover_{patient["ptName"]}.pdf', 'rb'), pdf.PdfFileReader(f'pacemaker_{patient["ptName"]}.pdf', 'rb')]
    elif (pwChoices == 3):
        pdfFiles = [pdf.PdfFileReader(f'faxcover_{patient["ptName"]}.pdf', 'rb'), pdf.PdfFileReader(f'anticoag_{patient["ptName"]}.pdf', 'rb')]
    elif (pwChoices == 4):
        pdfFiles = [pdf.PdfFileReader(f'faxcover_{patient["ptName"]}.pdf', 'rb')]
    for pdf in pdfFiles:
        mergeFile.append(pdf)
    names = patient['ptName'].split(' ')
    os.system('powershell rm *.docx')
    os.system('powershell rm *.pdf')
    mergeFile.write(f'Request- {names[1]}, {names[0]} med recs req.pdf')
    file2Fax = f"Request- {names[1]}, {names[0]} med recs req.pdf"
    print(type(str(file2Fax)))

    def faxIt(pt):
        fileFaxing = f"Request- {names[1]}, {names[0]} med recs req.pdf"
        phaxio = PhaxioApi('326hm7hwwjgtnh18qo66lauwmx4oc8wf2vbth6he', '014a3atyonq17kx4ftixk6orfs0addix5yowk9jd')
        phaxio.Fax.send(
            to='6233221504',
            files=fileFaxing
        )
    faxIt(patient)
    os.system(r"powershell mv *.pdf 'S:\'")



    return patient
main()








