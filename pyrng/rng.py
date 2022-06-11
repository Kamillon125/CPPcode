from random import randint
def rng(x):
    george = False
    if x == 1:
        value = randint(0, 8192)

    elif x == 2:
        value = randint(0, 4096)

    elif x == 3:
        value = randint(0, 2048)

    elif x == 4:
        value = randint(0, 1366)

    elif x == 5:
        value = randint(0, 1025)

    elif x == 6:
        value = randint(0, 819)

    elif x == 7:
        value = randint(0, 683)

    elif x == 8:
        value = randint(0, 586)

    if value == 1:
        george = True
    #match (switch) cases dont work in python 3.8
    return george
