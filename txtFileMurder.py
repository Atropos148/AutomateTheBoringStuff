#! python3
# DO NOT USE! NO WAY TO STOP IT!
import os

i = 0
x = 0
folder = 0
pathStart = '.\\txtMurder\\Murder0'
pathLorem = '.\\lorem.txt'

if not os.path.exists(pathStart):
    os.makedirs(pathStart)

if not os.path.exists(pathLorem):
    os.makedirs(pathLorem)

lorem = open(pathLorem).read().replace("\n", '').split()

print('exit to exit')

while True:
    path = ('.\\txtMurder\\Murder%s' % folder)
    pathFile =  path + ('.\\txtMurder%s.txt' % i)
    if not os.path.exists(path):
        os.makedirs(path)

    if os.path.isfile(pathFile):
        i += 1
    else:
        txtMurderFile = open(pathFile, 'w')
        for x in range(10):
            txtMurderFile.write(str(lorem))
        txtMurderFile.close()
        if i > 50:
            i = 0
            folder += 1
            print('Folder Done')
            if not os.path.exists(path):
                os.makedirs(path)
