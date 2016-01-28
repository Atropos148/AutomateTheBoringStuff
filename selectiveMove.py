#! python3

import shutil, os

folder = '.'
folder = os.path.abspath(folder)
wantedExtension1 = '.py'
wantedExtension2 = '.pyw'
newFolder = '.\\test\\'

if not os.path.exists(os.path.abspath(newFolder)):
    os.makedirs(os.path.abspath(newFolder))

for foldername, subfolders, filenames in os.walk(os.path.abspath(folder)):
    for filename in filenames:
        if filename.endswith(wantedExtension2):
            shutil.copy(filename, newFolder)
        elif filename.endswith(wantedExtension1):
            shutil.copy(filename, newFolder)
