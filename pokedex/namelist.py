
from re import search
def pokelist(): #returns list of pokemon names
    namelistarr = []
    f = open('namelist.txt', 'r')
    for line in f:
        length = len(line)
        namelistarr.append(line[:length - 1])
    f.close()
    return (namelistarr)

def hyphenlist(name): #searches for name if incorrect
    amountcount = 0
    the = []
    for i in pokelist():
        if search(name, i):
            the.append(i)
    string = ''
    for i in the:
        string += f'{i} '
        amountcount+=1
        if amountcount%10==0:
            string += '\n'

    return string