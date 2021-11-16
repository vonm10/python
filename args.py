def myfunc(input):
    letters = list(input)
    for i in range(0,len(letters)):
        if i%2!=0:
            letters[i] = letters[i].capitalize()
        else:
            continue
    return ''.join(letters)

print(myfunc("ahoj"))