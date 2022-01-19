import os
import subprocess
import shutil

userprof = os.environ['USERPROFILE']
print(f'The profile is: "{userprof}"')
ogFilePaths = [f'C://Users//OSC//Desktop/Medical Records PDFs/faxcover_Zack Hatch.pdf', f'C://Users//OSC//Desktop/Medical Records PDFs/anticoag_Zack Hatch.pdf', f'C://Users//OSC//Desktop/Medical Records PDFs/pacemaker_Zack Hatch.pdf']

for path in ogFilePaths:
    shutil.move(path, './')
os.system('cd C://Users//OSC//Desktop/Medical Records PDFs')
os.system('copy *.pdf "C://Users//OSC//Desktop/Python"')