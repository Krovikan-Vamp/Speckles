Copy-Item *.pdf "C:\Users\OSC\Four Peaks Surgery Center\SCANS - Documents\May Medical Records"
Write-Output "Copying to Sharepoint"
Copy-Item *.pdf "\\AUUAW1024F8\Users\OSC\OneDrive\Desktop\May Medical Records"
Write-Output "Copying to Fran's Backup"
Move-Item *.pdf S:\
Write-Output "Moving to Scans drive"