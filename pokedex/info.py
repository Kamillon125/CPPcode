import pypokedex
import idname


def basicinfo(id, arg):
    pokemon = pypokedex.get(name=idname.idtoname(id.lower()))
    types = ', '.join(pokemon.types).title()
    hiddenstring = ''
    normalstring = []
    for i in pokemon.abilities:
        if i.is_hidden == True:
            hiddenstring = i.name.replace('-', ' ')

        else:
            normalstring.append(i.name)
    if len(normalstring) == 1:
        normstring = f'{normalstring[0]}'
        normstring = normstring.title()
    else:
        normstring = f'{normalstring[0]}, {normalstring[1]}'
        normstring = normstring.title()
    if len(normalstring)==2:
        strang = f'Abilities - {normstring.replace("-", " ").title()}'
    else:
        strang = f'Ability - {normstring}'
    if len(hiddenstring) > 1:
        strang += f'\nHidden Ability - {hiddenstring.title()}'
    else:
        strang += f'\nHidden Ability - None'
    typeword = ''
    if len(pokemon.types) == 2:
        typeword = 'Types'
    else:
        typeword = 'Type'
    if arg == '1':
        return f'''{pokemon.name.title().replace('-', ' ')} - #{pokemon.dex}
HP - {pokemon.base_stats.hp}, 
Atk|SpAtk - {pokemon.base_stats.attack}|{pokemon.base_stats.sp_atk}, 
Def|SpDef - {pokemon.base_stats.defense}|{pokemon.base_stats.sp_def}, 
Spd - {pokemon.base_stats.speed}'''

    else:
        return f'''{pokemon.name.title().replace('-', ' ')} - #{pokemon.dex}
Height - {float(pokemon.height) / 10} m | Weight - {float(pokemon.weight) / 10} kg
{typeword} - {types}
{strang}
HP - {pokemon.base_stats.hp}, 
Atk|SpAtk - {pokemon.base_stats.attack}|{pokemon.base_stats.sp_atk}, 
Def|SpDef - {pokemon.base_stats.defense}|{pokemon.base_stats.sp_def}, 
Spd - {pokemon.base_stats.speed}'''
