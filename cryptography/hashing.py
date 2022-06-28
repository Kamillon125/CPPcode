from hashlib import sha256
import time
def hash(x):
    return sha256(x.encode('utf-8')).hexdigest()

def checkinput(x):
    if not x.isdigit():
        return False
    if int(x) < 1 or int(x) > 1579:
        return False
    return True

def write(x):
    with open('hash.txt', 'w') as file:
        file.write(hash(x[0]) + '\n')
        file.write(hash(x[1]))

def detect():
    with open('hash.txt', 'r') as file:
        arg = []
        for line in file:
            arg.append(line)
        return '\n'.join(arg)

x = str(input('Tell me 2 numbers between 0 and 1589 that are meant to be hashed separated by space '))
args = list(x.split(' '))
while checkinput(args[0]) == False or checkinput(args[1]) == False:
    x = str(input('Input incorrect '))
    args = list(x.split(' '))
write(args)
time.sleep(5)
print(detect(), end='')
