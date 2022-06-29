from cryptography.fernet import Fernet
import os
def genkey2():
    key = b'RI7tswlb4lB9gPNDMMfO4nMxKzUFLcL8ZzqDKqKlLaw='
    return key
key = genkey2()
def genkey():
    key = b'RI7tswlb4lB9gPNDMMfO4nMxKzUFLcL8ZzqDKqKlLaw='
    f = Fernet(key)
    return f
f = genkey()

def getpass():
    arg = []
    with open('passcode.txt', 'r') as file:
        for line in file:
            if len(arg) == 0:
                arg = line
                return arg

def code(x):
    key = genkey2()
    f = Fernet(key)
    george = f.encrypt(bytes(x, 'utf-8'))
    return str(george)

def setmaster():
    global inputting
    game = True
    while game == True:
        inputting = str(input('Set your new master password.\n'))
        inputt = str(input(f'Are you sure you want {inputting} to be your master password? y/n\n'))
        if inputt == 'y':
            game = False
            break
    with open('passcode.txt', 'w') as file:
        chacha = code(inputting.replace('\n', " "))
        chachacha = chacha[2:-1]
        file.write(chachacha)
    return inputting

def readpw():
    if os.path.getsize('passwords.txt') == 0:
        print('No passwords detected.')
        return 0
    else:
        with open('passwords.txt', 'r') as file:
            for line in file:
                #print(bytes(line[:-1], 'utf-8'))
                print(str(f.decrypt(bytes(line[:-1], 'utf-8')).decode()))
        return 0

def addpw():
    website = str(input('What website would you like to add a password for? '))
    pw = str(input('What would you like your password to be? '))
    string = f'{website}: {pw}'
    with open('passwords.txt', 'a') as file:
        file.write(str(f.encrypt(bytes(string, 'utf-8')))[2:-1] + '\n')
    return string

def check():
    if os.path.getsize('passcode.txt') == 0 and os.path.getsize('passwords.txt') == 0:
        setmaster()
    elif os.path.getsize('passcode.txt') == 0 and os.path.getsize('passwords.txt') > 0:
        print('Detected discrepancies. Deleting all passwords.')
        with open('passwords.txt', 'w') as file:
            file.close()
        quit()
    else:
        return 0

def command():
    user = str(input(f'''Would you like to:
    (1) See all passwords
    (2) Add password\n'''))
    while user != '1' and user != '2':
        user = str(input('Incorrect input. '))
    if user == '2':
        addpw()
    elif user == '1':
        readpw()

def checkmasterpassword():
    masterpassworde = bytes(getpass(), 'utf-8')
    masterpassword = str(f.decrypt(masterpassworde).decode())
    userpass = str(input('What is your master password? '))
    passtoken = f.encrypt(bytes(masterpassword, 'utf-8'))
    fishtoken = f.encrypt(bytes(userpass, 'utf-8'))
    decrypted = str(f.decrypt(passtoken).decode())
    while userpass != decrypted:
        masterpassworde = bytes(getpass(), 'utf-8')
        masterpassword = str(f.decrypt(masterpassworde).decode())
        userpass = str(input('What is your master password? '))
        passtoken = f.encrypt(bytes(masterpassword, 'utf-8'))
        fishtoken = f.encrypt(bytes(userpass, 'utf-8'))
        decrypted = str(f.decrypt(passtoken).decode())
        userpass = 'Master password incorrect. '
    return 0


def test():
    che = bytes(getpass(), 'utf-8')
    password = str(f.decrypt(che).decode())

    inputs = str(input('What is your master password? '))

    passtoken = f.encrypt(bytes(password, 'utf-8'))

    fishtoken = f.encrypt(bytes(inputs, 'utf-8'))

    decrypter = str(f.decrypt(passtoken).decode())
    while inputs != decrypter:
        inputs = str(input('Master password incorrect. '))
    return 0
game = True
count = 0
while game == True:
    check()
    if count == 0:
        test()
    count +=1
    command()
    user = str(input('Continue? y/n: '))
    if user == 'n':
        quit()


