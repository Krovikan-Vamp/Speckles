# Medical Records Python Scripts

A quick overview on the installation process and usage of the `docx-test.py` script. Other scripts in this repository are older versions using terribly outdated tactics to achieve the same goal. Contact the [creator](https://github.com/Krovikan-Vamp) with question about their processes.

## Installation

1. Make sure [Python](https://www.python.org/downloads/) version >= 3.10.1 is installed locallay
    - This requires administrator privileges on company/AUUA machines
    - Contact Zack to install Python on another user to keep OSC user non-admin
    - Make sure Python was added to PATH env variable
2. Clone the [repository](https://github.com/Krovikan-Vamp/Python/) to the desired path
3. Download [Visual Studio Code](https://code.visualstudio.com/) as an administrator 

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

