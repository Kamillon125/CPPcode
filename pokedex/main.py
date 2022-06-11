import validchecker
import moves
import gen
import info
splitchar = '.'
x = 0
game = True
def validcheck(arg):
    valid = ['bst', 'move', 'info']
    if arg in valid:
        return True
    else:
        return False

def movelookup():
    string = input('''\nWhich pokemons moves would you like to look up?
Input Pokemon name/Dex number, the character '.' and game (ie: Pikachu.sun) ''')
    args = string.split(splitchar)
    args = validchecker.checkvalid(args, x, splitchar)
    print(moves.movegetter(args[0], gen.genconverter(args[1])[1]))

def infolookup(y):
    string = input('''\nWhich pokemons basic information would you like to look up?
Input Pokemon name/Dex number. ''')
    while validchecker.validchecker(string, 0)[0] == '0':
        string = input(validchecker.validchecker(string, 0)[1])
    print(info.basicinfo(string.lower(), y))

while game == True:

    arg = str(input('''\nWould you like to:
Look up the basic information of a Pokemon? Input info
Look up the learnset of a Pokemon in a certain game? Input move 
Look up the base stat total of a Pokemon? Input bst\n'''))
    while validcheck(arg.lower().replace(' ', '')) == False:
        arg = str(input('Input not recognised. '))
    arg = arg.lower().replace(' ', '')
    if arg == 'move':
        movelookup()
    elif arg == 'bst':
        infolookup('1')
    elif arg == 'info':
        infolookup('0')





