import pypokedex
import idname


def movegetter(id, game): # This function gets the moves of a pokemon in a certain game
    pokemon = pypokedex.get(name=idname.idtoname(id.lower())) #gets pokemon object based on name given
    levelup = []
    machine = []
    tutor = []
    for i in pokemon.moves.get(game):
        if i.learn_method == 'level-up':
            if i.level != None:
                levelup.append(i)
        elif i.learn_method == 'machine':
            machine.append(i)
        elif i.learn_method == 'tutor':
            tutor.append(i)
    try:
        levelup.sort(key=lambda x: x[2])
    except:
        return '''Something went wrong while sorting level up moves. The Pokemons move learnset cannot be returned. '''
    gamename = game.title().replace('-', ' and ')

    string = f'\n{pokemon.name.title().replace("-", " ")} learns these moves in {gamename}:\n'
    number = 0
    if len(levelup)>0:
        string += 'Moves learnt by level up:\n'
        for i in levelup:
            if i.level < 10:
                string += f' {i.level} {i.name.title().replace("-", " ")} \n'
            else:
                string += f'{i.level} {i.name.title().replace("-", " ")} \n'
    if len(machine)>0:
        string += '\nMoves learnt by TM\n'
        for i in machine:
            string += f'{i.name.title().replace("-", " ")}. '
            number+= 1
            if number%10==0:
                string += '\n'
    if len(tutor)>0:
        string += '\n\nMoves learnt by tutor\n'
        vnumber = 0
        for i in tutor:
            string += f'{i.name.title().replace("-", " ")}. '
            vnumber += 1
            if vnumber % 10 == 0:
                print('\n')
    return string