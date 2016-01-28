#! python3
# backupToZip.py - semi-auto backup system, makes a backup of folder to numbered zip

import zipfile, os

def backupToZip(folder):
    # backup whole folder to zip file
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename), compress_type=zipfile.ZIP_DEFLATED)

    backupZip.close()
    print('Done')

backupToZip('C:\\bitbucket\\python3training')