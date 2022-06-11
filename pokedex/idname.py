import pypokedex
import namelist
def idtoname(id):
    if id.isnumeric() == True: #checks if user input is dex id
        id = int(id)
    if type(id) == int or type(id) == float:
        if int(id) < 899 and int(id)>0:
            pokename = pypokedex.get(dex=id).name
        else:
            return 'rockruff'
    else:
        pokename = id
        if pokename not in namelist.pokelist():
            return False
    pokename = pokename.lower()
    return pokename