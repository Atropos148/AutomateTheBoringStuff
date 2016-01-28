#! python3

import os

print('Which drive you want to check?')

while True:
    choice = input()
    if choice == 'c':
        folder = 'C:\\'
        folder = os.path.abspath(folder)
        print('Biggest files on C:')
        break
    elif choice == 'd':
        folder = 'D:\\'
        folder = os.path.abspath(folder)
        print('Biggest files on D:')
        break
    else: print('Use lowercase letters')


for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        path = os.path.join(foldername, filename)
        if os.path.exists(path):
            if path.endswith('.dat') or path.endswith('.DAT') or path.endswith('.assets') or path.endswith('.exe') or path.endswith('.a') or path.endswith('.mix') or path.endswith('.ff'):
                continue
            else:
                fileSize = round((os.path.getsize(path))/1000000, 2)
                if fileSize > 100:
                    if fileSize > 1000:
                        fileSize /= 1000
                        print(os.path.abspath(path) + ' ' + str(round(fileSize, 2)) + ' Gigabytes')
                    else: print(os.path.abspath(path) + ' ' + str(fileSize) + ' Megabytes')

print('Done!')
