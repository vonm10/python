with open('txt.txt') as myFile:
    contents = myFile.read()

with open('txt.txt',mode='a') as myFile:
    myFile.write('\nkkkk')

myList = [1,2,3]
for item in myList:
    print(item)

def say_hello(name='Default'):
    print('Hello {}'.format(name))
say_hello('Matyas')
say_hello()