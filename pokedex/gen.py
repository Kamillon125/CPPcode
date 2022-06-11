def genconverter(game): #a trainwreck of a function, converts user input to usable game name
    strang = '''Here are the acceptable game inputs:
red, blue, yellow, 
gold, silver, crystal, 
ruby, sapphire, emerald, 
diamond, pearl, platinum, 
heartgold, soulsilver, hg, ss, 
black, white, black2, white2,
x, y,
omegaruby, alphasapphire, or, as,
sun, moon, ultrasun, ultramoon, us, um,
letsgopikachu, letsgoeevee, lgpe, letsgo
sword, shield, swsh, 1, 2, 3, 4, 5, 6, 7, 8
Input the whole string again: '''
    game = game.replace(' ', '')
    if game == 'red' or game == 'blue' or game == '1':
        return ['1', 'red-blue']
    if game == 'yellow':
        return ['1', 'yellow']
    if game == 'gold' or game == 'silver' or game == '2':
        return ['1', 'gold-silver']
    if game == 'crystal':
        return ['1', 'crystal']
    if game == 'ruby' or game == 'sapphire' or game == '3':
        return ['1', 'ruby-sapphire']
    if game == 'emerald':
        return ['1', 'emerald']
    if game == 'diamond' or game == 'pearl' or game == '4':
        return ['1', 'diamond-pearl']
    if game == 'platinum':
        return ['1', 'platinum']
    if game == 'heartgold' or game == 'soulsilver' or game == 'hg' or game == 'ss':
        return ['1', 'heart-gold-soul-silver']
    if game == 'black' or game == 'white' or game == '5':
        return ['1', 'black-white']
    if game == 'black2' or game == 'white2':
        return ['1', 'black-2-white-2']
    if game == 'x' or game == 'y' or game == '6':
        return ['1', 'x-y']
    if game == 'omegaruby' or game == 'alphasapphire' or game == 'or' or game == 'as':
        return ['1', 'omega-ruby=alpha-sapphire']
    if game == 'sun' or game == 'moon' or game == '7':
        return ['1', 'sun-moon']
    if game == 'ultrasun' or game == 'ultramoon' or game == 'us' or game == 'um':
        return ['1', 'ultra-sun-ultra-moon']
    if game == 'sword' or game == 'shield' or game == 'swsh' or game == '8':
        return ['1', 'sword-shield']
    if game == 'letsgopikachu' or game == 'letsgoeevee' or game=='lgpe' or game=='letsgo':
        return ['1', 'lets-go-pikachu-lets-go-eevee']
    else:
        return ['0', strang]