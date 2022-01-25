physician = {
        "drName": input(f'What is the name of the doctor you are contacting? (Name only! No "Dr." needed!)\n'),
        "pNumber": input(f'What is the phone number of the facility you are faxing?\n'),
        "fNumber": input(f'What is the number you are faxing to?\n'),
    }
    # prompt['docs'].append('Faxcover')
patient = {
# "forms": prompt["docs"],
"ptName": input(f'What is the name of the patient?\n'),
"dateOfBirth": input(f"What is the patient's date of birth?\n"),
"yourName": 'Zackery H./Franchesca G.',
"procedureDate": input(f'What is the date of the procedure?\n'),
"procedureName": input(f'What is the procedure name? (i.e. PVP (Photovaporization of the prostate))\n'),
"anesthesiologistName": input(f'Who is the surgeon? (Kaplan, Wong...)\n'),
# "dateOfFax": dt.today().strftime("%B %d, %Y"),
"physicians": [],
# "numberOfPages": str(len(docs)),
"urgency": 'URGENT',
}
patient['physicians'].append(physician)
patient['physicians'].append(physician)
print(patient['physicians'])