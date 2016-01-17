spam = ['apples', 'bananas', 'tofu', 'cats']
hugeList = ['car','house','cat','furry','bet','sack','high','like','Mike']
print('Lists:')
print('1.spam' + ' ' + '2.hugeList')
while True:
    print('What list do you want?')
    choice = input()
    if choice == '1':
        list = spam
        break
    elif choice == '2':
        list = hugeList
        break
    else:
        print('Bad input')


for i in range(len(list)):
    if i == (len(list)-1):
        print(list[i],end='')
    elif i == (len(list)-2):
        print(list[i],end=' and ')
    elif i < len(list):
        print(list[i],end=', ')