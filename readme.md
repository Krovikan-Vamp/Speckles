# Medical Records Python Scripts

A quick overview on the installation process and usage of the `docx-test.py` script. Other scripts in this repository are older versions using terribly outdated tactics to achieve the same goal. Contact the [creator](https://github.com/Krovikan-Vamp) with question about their processes.

## Installation

1. Make sure [Python](https://www.python.org/downloads/) version >= 3.10.1 is installed locallay
    - This requires administrator privileges on company/AUUA machines
    - Contact Zack or IT support (XLCON) to install Python on another user to keep OSC user non-admin
    - Make sure Python was added to PATH env variable
2. Clone the [repository](https://github.com/Krovikan-Vamp/Python/) to the desired path
3. Download [Visual Studio Code](https://code.visualstudio.com/) as an administrator 
4. Request a Service Account key from the [administrator](https://github.com/Krovikan-Vamp)
    - Ensure the Account key is stored in the root directory of the cloned repository.

## Using the Script

1. Open Visual Studio Code
2. Open the folder where the repository was cloned
    - `Ctrl + K & Ctrl + O`
3. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-environment-manager) from the Marketplace
4. Press the ![image](https://user-images.githubusercontent.com/97307321/151602968-28d6eaeb-b17b-4055-b4e5-f0865c72a8e6.png) button in the top right to run the script within the integrated terminal
5. Follow the steps!

## Script Instructions

1. The following questions will be prompted to the user
    > ![image](https://user-images.githubusercontent.com/97307321/151602884-4a5c52ae-afc7-4c9b-abb9-596e03dd7649.png) <br />
    > ![image](https://user-images.githubusercontent.com/97307321/151603137-4932240c-09af-46ea-88c4-ea063c67f32a.png)
2. Fill out the prompted information
3. The script will do the following
    - Fill out the selected word docs queried by the [first question](https://user-images.githubusercontent.com/97307321/151602884-4a5c52ae-afc7-4c9b-abb9-596e03dd7649.png)
    - Create PDF files out of the documents edited using [Py2PDF](https://pypi.org/project/py2pdf/)
    - Delete created temporary files (.pdf & .docx)
    - Merges and saves the files to a single, correctly named ('Request- Last, First Med Recs Req.pdf') files using [PyPDF2](https://pypi.org/project/PyPDF2/)
    - Writes the properties of the `dict` to a new .xlsx file with the same name as the PDF using [openpyxl](https://pypi.org/project/openpyxl/)

## Upcoming features

Features that are new or in the process of being implemented. These features are currently *Work in Progress* and still require patching to work properly but are plausible.

### Faxing

With all of this time saved using this script, the only piece of the puzzle left is to fax and receive files. This can be achieved using an API called [Phaxio](https://www.phaxio.com/). The required code to send the file created by this file has been commented out from the [main file](https://github.com/Krovikan-Vamp/Python/blob/master/docx-test.py) and can be seen below...

```Python
import phaxio

def faxIt(pt):
    fileFaxing = f"Request- Last, First Med Recs Req.pdf"
    phaxio = PhaxioApi('apiKEY', 'apiSECRET')
    phaxio.Fax.send(
        to='receivingNumber',
        files=fileFaxing
    )
faxIt(patient)
```

### Auto-Completion and Suggestions

Another way to save time creating and sending out medical records is to auto-complete prompts given to the user. These include the surgeon, contacted physician name, phone, and fax numbers. 

Starting 1/31/2022 all data (physician name, phone, and fax numbers) submitted by the user will be stored in a [Firebase Firestore](https://firebase.google.com/products/firestore) database to be used by the program further. To provide the ability to use a new function [prompt](https://python-prompt-toolkit.readthedocs.io/en/master/index.html?) [python-prompt-toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/) was the go-to choice for autocompletion.

1. The first thing to do is grab all of the data from the database to create the suggestions with the [toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/index.html).
```Python
firebase_admin.initialize_app(credentials.Certificate('./sa.json'))
db = firestore.client()

# Create Suggestions
raw_docs = db.collection(u'Auto Suggestions').stream()
```

2. Next step is aggregate the data to work with the [WordCompleter](https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/prompt_toolkit/completion/word_completer.py) function.
```Python
docs = []
suggestion_list = {'fax': [], 'phone': [], 'dr': [], 'procedure': [], 'surgeons': [
    'LaTowsky', 'Mai', 'Kaplan', 'Kundavaram', 'Stern', 'Klauschie', 'Schlaifer', 'Jones', 'Wong', 'Devakumar']}

# Makes the docs usable as dicts
for doc in raw_docs:
    docs.append(doc.to_dict())

keys = ['fax', 'phone', 'dr', 'procedure']
for doc in docs:
    for key in keys:
        suggestion_list[key].append(doc[key])
```

3. Following the aggregation of the data, implement it in the prompts given to the user.
```Python
patient = {
    "ptName": prompt(f'What is the name of the patient?\n'),
    "dateOfBirth": prompt(f"What is the patient's date of birth?\n"),
    "procedureDate": prompt(f'What is the date of the procedure?\n'),
    "procedureName": prompt(f'What is the procedure name? (i.e. PVP (Photovaporization of the prostate))\n', completer=FuzzyCompleter(WordCompleter(suggestion_list['procedure'])), complete_in_thread=True, complete_while_typing=True),
    "anesthesiologistName": prompt(f'Who is the surgeon? (Kaplan, Wong...)\n', completer=FuzzyCompleter(WordCompleter(suggestion_list['surgeons'])), complete_in_thread=True, complete_while_typing=True),
    "drName": prompt(f'What is the name of the doctor you are contacting? (Name only! No "Dr." needed!)\n', completer=FuzzyCompleter(WordCompleter(suggestion_list['dr'])), complete_in_thread=True, complete_while_typing=True),
    "pNumber": prompt(f'What is the phone number of the facility you are faxing?\n', completer=FuzzyCompleter(WordCompleter(suggestion_list['phone'])), complete_in_thread=True, complete_while_typing=True),
    "fNumber": prompt(f'What is the number you are faxing to?\n', completer=FuzzyCompleter(WordCompleter(suggestion_list['fax'])), complete_in_thread=True, complete_while_typing=True),
    "forms": og_prompt["docs"],
    "dateOfFax": dt.today().strftime("%B %d, %Y"),
    "numberOfPages": str(len(docs)),
    "urgency": 'URGENT',
    "yourName": 'Names',
}
```
   * FuzzyCompleter is used to allow the typing of for example 8835 and the suggestions to populate with everything containing 8835... Such as (623 876 8835, 623 883 5824)

4. The new suggestions will populate like this

![image](https://user-images.githubusercontent.com/97307321/151882380-cc661562-9a66-444e-b424-fab36dd1b180.png)
![image](https://user-images.githubusercontent.com/97307321/151882308-65956c20-d38a-4113-a938-607a84b77bcc.png)

5. The 5th and final step is the new suggestions to the database to further improve the suggestions

```Python 
new_info = {'fax': patient['fNumber'], 'phone': patient['pNumber'],
            'dr': patient['drName'], 'procedure': patient['procedureName']}
db.collection('Auto Suggestions').document().set(new_info)
```

