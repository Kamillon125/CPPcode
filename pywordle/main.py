import random
from collections import Counter

file = open('wordleanswerlist.txt', 'r')
answerlist = []
for line in file:
    answerlist.append(line[:5])

files = open('words.txt', 'r')
wordlist = []
for line in files:
    wordlist.append(line[:5])

def checkunique(str):
  for i in range(len(str)):
    for j in range(i + 1,len(str)):
      if(str[i] == str[j]):
        return False
  return True

def freq(words): # checks the frequency of all letters in the list given to it
    gorg = ''
    chars = ''.join(words)
    nchars = len(chars)
    frequency = []
    counter = Counter(chars)
    occpct = [(char, occ / nchars * 100) for char, occ in counter.most_common()]
    for occ, pct in occpct:
        frequency.append(occ)
        #print(occ, f'{pct:.2f}%') this used to print out the letters with their frequencies in %
    return frequency

def freqdisplay(words):
    gorg = ''
    chars = ''.join(words)
    nchars = len(chars)
    frequency = []
    counter = Counter(chars)
    occpct = [(char, occ / nchars * 100) for char, occ in counter.most_common()]
    for occ, pct in occpct:
        frequency.append(occ)
        print(occ, f'{pct:.2f}%')
    print('''
    ''')

def remove(list, unwanted): # removes unwanted characters from a list
    list = [e for e in list if e not in unwanted]
    return list

def validitychecker(wordslist): # checks the validity of wordle words given to it
    if len(wordslist)>6:
        return False
    for i in wordslist:
        if len(i)!=5:
            return False
        if i not in wordlist:
            return False
    return True

def letterchecker(words): # checks what leters there are in a list parsed to it, then returns repeated letters, unique letters and total letters
    letterslist = []
    uniqueletterslist = []
    repeatletterslist = []
    for x in words:
        for i in x:
            if i not in letterslist and i != ' ':
                uniqueletterslist.append(i)
            if i in letterslist and i != ' ':
                repeatletterslist.append(i)
            if i !=' ':
                letterslist.append(i)
    return letterslist, uniqueletterslist, repeatletterslist

def appender(lists): #appends list into a string (ie: ['short', 'plane'] -> shortplane
    stromg = ''
    for i in lists:
        stromg = stromg + i
    return(stromg)

def letterevaluation(l, u, r): #evaluates wordle letters
    if len(r)==0:
        strang = f'''In total you have:
                {len(l)} total letters, which are {appender(l)}
                {len(u)} unique letters, which are {appender(u)}
                0 repeated letters
            '''
    else:
        if len(r)>1:
            cheez, cheese = 'letters', 'are'
        else:
            cheez, cheese='letter', 'is'
        strang = f'''In total you have:
                    {len(l)} total letters, which are {appender(l)}
                    {len(u)} unique letters, which are {appender(u)}
                    {len(r)} repeated {cheez}, which {cheese} {appender(r)}
                    '''
    return(strang)

def trydesperately(letterlist, words): #for when genwords doesnt work
    pb = 0
    sir = 0
    jorge = ''
    for x in words:
        sir = 0
        for i in x:
            if i in letterlist:
                sir+=1
            if sir > pb:
                pb = sir
                jorge = x
    return f'''The word that would be the best addition to your strategy is {jorge}'''

def genwords(letterlist, words): #generates extra words for the strat
    if len(letterlist) < 5:
        return 'There are less than 5 letters of the alphabet left, so no words can probably be formed exclusively with them.'
    jorge = ''
    fish = False
    g = 5
    count = 0
    stronmg = 'We could not find another word to add to your strategy.'
    while fish == False:
        for x in words:
            for i in x:
                if all([char in letterlist for char in x]):
                    if checkunique(x) == True and count==0:
                        jorge=jorge + x
                        count+=1
        if g == len(letterlist) and len(jorge) == 0:
            return trydesperately(letterlist, words)
        elif len(jorge) == 0:
            g = g+1
        elif len(jorge) !=0:
            return f'''The word that would be the best addition to your strategy is {jorge}'''

def analysewordle():
    game = True
    start = 0
    while game == True:
        if start == 0:
            wordies = str(input(f'''Input your wordle starting words separated by space, 
example - short plane brick ''')).lower()
        else:
            wordies = str(input('Input your wordle strategy again '))
        while validitychecker(wordies.lower().split(' ')) == False:
            wordies = str(
                input('Please input 6 or less words that are 5 letters long and in the word list for wordle. ')).lower()
        l, u, r = letterchecker(wordies)
        print(letterevaluation(l, u, r))
        letters = remove(freq(answerlist), l)  # unused letters from the alphabet after putting in our query
        if len(wordies.split(' '))<6:
            print(genwords(letters, wordlist))
        else:
            print('''You have 6 words already, but despite that''')
            print(genwords(letters, wordlist))
        start +=1
        play = str(input('Would you like to go again? enter if yes, type anything else if no '))
        if play != '':
            game = False

strang = '''Hey. Let's play wordle.
For every letter you get in its correct place, I will display an X.
For every letter you get that is in the word, but is in another position, I will display a Y.
For every letter you guess that is not in the word, I will display an O.
Guess a 5 letter word.
'''

def split(word):
    return list(word)

def wordpicker():
    n = random.randint(1, len(answerlist)-1)
    return answerlist[n]

def listtostring(string):
    str1=', '
    fancystring = str1.join(string)
    newstring = ''
    for i, letter in enumerate(fancystring):
        if i % 70 == 0:
            newstring +='\n'
        newstring += letter
    newstring = newstring[1:]
    return newstring

def runwordlewords(choose):
    playing = True
    while playing == True:
        try:
            int(choose)
            itis = True
        except ValueError:
            itis = False
        if itis == False:
            choose = 100
        else:
            choose = abs(int(choose))
        filething = []
        repeats = []
        gorgfish = 0
        gorgfash = 0
        for i in range(0, choose):
            gorg = wordpicker()
            if gorg in filething:
                gorgfish += 1
                filething.append(gorg)
                if gorg not in repeats:
                    repeats.append(gorg)
                    gorgfash += 1
            else:
                filething.append(gorg)
        print(listtostring(filething))
        print(f'\nThere were {gorgfish} repeated words in that list.\n')
        if gorgfish > 0:
            if gorgfish == 1:
                print(f'The repeated word was {listtostring(repeats)}')
            print(f'Unique repeated words, of which there were/was {gorgfash}, were: \n{listtostring(repeats)}\n')
            asker = str(input('Would you like to play again? Press enter if yes and type anything else if no '))
            if asker != '':
                return 0

def wordchecker(word, cword):
    x = split(word.lower())
    y = split(cword.lower())
    id = ['O', 'Y', 'X']
    wordthing = ''
    for i in range(0, len(x)):
        if x[i]==y[i]:
            wordthing = wordthing + id[2] + ' '
        elif x[i] in y:
            wordthing = wordthing + id[1] + ' '
        else:
            wordthing = wordthing + id[0] + ' '
    return wordthing

def wordtracker(word, cword):
    x = split(word.lower())
    y = split(cword.lower())
    knownletters = ''
    for i in range(0, len(x)):
        if x[i]==y[i]:
            knownletters = knownletters + x[i].upper()
        elif x[i] in y:
            knownletters = knownletters + x[i].lower()
    return knownletters

def checkifwordiscorrect(word, wordsused):
    characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    error = 0
    for i in word:
        if i not in characters:
            error = 1
    if len(word)!=5 or error == 1:
        print('Error: The word must be 5 characters long and only contain letters.')
        return False
    if word.lower() not in wordlist:
        print('Error: Use a valid word.')
        return False
    return True

def wordle(choose):
    play = True
    while play == True:
        try:
            int(choose)
            itis = True
        except ValueError:
            itis = False
        if itis == False:
            choose = 0
        else:
            choose = abs(int(choose))
        word = str(input(strang))
        cword = wordpicker()
        playing = True
        attemptcount = 1
        wordsused = []
        guessed = []
        while playing == True:
            if word in wordsused:
                word = str(input(''))
            while checkifwordiscorrect(word, wordsused) != True:
                word = str(input(''))
            print(wordchecker(word, cword), wordtracker(word, cword))
            wordsused.append(word)
            guessed.append(wordchecker(word, cword))
            thingymajig = ''
            if attemptcount == 1:
                thingymajig = 'try'
            else:
                thingymajig = 'tries'
            if wordchecker(word, cword) == 'X X X X X ':
                print(f'Congratulations, you guessed the word! It took you {attemptcount} {thingymajig}.')
                for i in range(0, len(wordsused)):
                    print(guessed[i], wordsused[i])
                asker = str(input('Would you like to play again? Press enter if yes and type anything else if no '))
                if asker != '':
                    return 0
                else:
                    playing = False
            if attemptcount == choose and choose != 0:
                print(f'You unfortunately lost in {choose} {thingymajig}. The word was {cword}.')
                for i in range(0, len(wordsused)):
                    print(guessed[i], wordsused[i])
                asker = str(input('Would you like to play again? Press enter if yes and type anything else if no '))
                if asker != '':
                    return 0
                else:
                    playing = False
            else:
                attemptcount += 1

while True:
    choose = str(input('''
Hi, would you like to:
Play wordle? - Press enter.
Generate a certain amount of wordle words? - Type gen and press enter.
Have your wordle strategy judged? Type judge and press enter.
Generate the letter frequency of wordle words? Type freq and press enter.
If you would like to exit the program, type the word exit and press enter. '''))
    if choose == '':
            choose = input('How many guesses would you like the limit to be? Type anything but an integer if you would like to have unlimited guesses. ')
            wordle(choose)
    elif choose.lower()=='exit':
        quit()
    elif choose.lower()=='gen':
        choose = str(input('How many wordle words would you like to generate? 100 by default '))
        runwordlewords(choose)
    elif choose.lower()=='judge':
        analysewordle()
    elif choose.lower()=='freq':
        freqdisplay(answerlist)
