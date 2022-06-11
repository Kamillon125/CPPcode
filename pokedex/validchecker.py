import namelist
import gen
import exists

def checkvalid(args, x, splitchar):
    checking = True
    while checking == True:
        while len(args) != 2:
            string = input('Please input two queries - the name/ID and the game. ')
            args = string.split(splitchar)

        while validchecker(args[0].lower(), x)[0] == '0' or gen.genconverter(args[1].lower())[0] == '0' or exists.exists_in(args[0].lower(), args[1].lower())[0] == '0':
            x +=1 #makes it so that 'are you sure you did not mean one of these:' message doesnt pop up 3 times
            if validchecker(args[0].lower(), x)[0] == '0' and gen.genconverter(args[1].lower())[0] == '1':
                string = input(validchecker(args[0].lower(), x)[1])
                args = string.split(splitchar)
                while len(args) != 2:
                    string = input('Please input two queries - the name/ID and the game. ')
                    args = string.split(splitchar)

            elif validchecker(args[0].lower(), x)[0] == '1' and gen.genconverter(args[1].lower())[0] == '0':
                string = input(gen.genconverter(args[1].lower())[1])
                args = string.split(splitchar)

                while len(args) != 2:
                    string = input('Please input two queries - the name/ID and the game. ')
                    args = string.split(splitchar)

            elif validchecker(args[0].lower(), x)[0] == '0' and gen.genconverter(args[1].lower())[0] == '0':
                string = input('Both the Pokemon name and the game name are incorrect. Input both again. ')
                args = string.split(splitchar)

                while len(args) != 2:
                    string = input('Please input two queries - the name/ID and the game. ')
                    args = string.split(splitchar)
            elif validchecker(args[0].lower(), x)[0] == '1' and gen.genconverter(args[1].lower())[0] == '1' and exists.exists_in(args[0].lower(), args[1].lower())[0] == '0':
                string = input('The Pokemon does not exist in this game. ')
                args = string.split(splitchar)

                while len(args) != 2:
                    string = input('Please input two queries - the name/ID and the game. ')
                    args = string.split(splitchar)

        return args

def validchecker(id, amountcount): #checks if pokedex id is within range, if name consists only of letteers and hyphens.
    characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-'
    if id.isnumeric():
        id = int(id)
        if id > 899 or id <0:
            return ['0', 'Pokedex ID out of range (1-898). ']
    else:
        for i in id:
            if i not in characters:
                return ['0', 'The pokemon name can only contain letters and hyphens. ']
        id = id.lower()
        pokename = id
        if pokename not in namelist.pokelist():
            if namelist.hyphenlist(pokename):
                return ['0', f'''Name not recognised. Are you sure you did not mean one of these: {namelist.hyphenlist(pokename)[:-1]} ''']
            return ['0', 'Pokemon name not detected. ']
    return '1'