import math
import re
def checker(id):
    characters = ['qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']
    num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
    isnumber = re.match(num_format, id)
    if isnumber:
        id = abs(float(id))
        if id > 898:
            id = math.floor(id)
        elif id < 1:
            id = math.ceil(id)
        else:
            id = math.ceil(id)
    else:
        for i in id:
            if i not in characters:
                return False
