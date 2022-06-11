import pypokedex
import gen
import namelist
def exists_in(id, game):
    if id.isnumeric() == True:
        id = int(id)
    if type(id) == int or type(id) == float:
        if int(id) < 899 and int(id) > 0:
            pokename = pypokedex.get(dex=id).name
        else:
            return False
    else:
        pokename = id
        if pokename not in namelist.pokelist():
            return False
    pokemon = pypokedex.get(name = pokename)
    game = gen.genconverter(game)[1]
    if pokemon.exists_in(game):
        return ['1', '']
    else:
        return ['0', 'The Pokemon does not exist in this game. ']