from random import seed
import rng
import secrets
from scipy.stats import binom
seed(secrets.randbelow(1_000_000_000))



def rolled(x, rolls):
    if x =='1':
        method = 'Gen 2-5 with full odds'
        avg = 8192
        if rolls > 8192:
            word = 'over'
        elif rolls < 8192:
            word = 'under'
        elif rolls == 8192:
            word = 'on'
    elif x =='2':
        method = 'Gen 6 onwards with full odds'
        avg = 4096
        if rolls > 4096:
            word = 'over'
        elif rolls < 4096:
            word = 'under'
        elif rolls == 4096:
            word = 'on'
    elif x == '3':
        method = 'Gen 8 with full odds'
        avg = 875
        if rolls > 875:
            word = 'over'
        elif rolls < 875:
            word = 'under'
        elif rolls == 875:
            word = 'on'
    odds = 1 - binom.cdf(k=0, n=int(rolls), p=(1/avg))
    print(f'''    You caught a shiny in {method} in {rolls} attempts. 
    You were {word} odds by {abs(avg - rolls)}
    At {rolls} attempts you had a {odds*100}% chance of having gotten it already''')

def roll(x):
    rolls = 0
    if x == '1':
        while True:
            rolls+=1
            if rng.rng(1):
                rolled(x, rolls)
                break
    elif x == '2':
        while True:
            rolls+=1
            if rng.rng(2):
                rolled(x, rolls)
                break
    elif x == '3':
        while True:
            if rolls<1:
                rolls+=1
                if rng.rng(2):
                    rolled(x, rolls)
                    break
            elif rolls>= 1 and rolls<50:
                rolls += 1
                if rng.rng(3):
                    rolled(x, rolls)
                    break
            elif rolls>=50 and rolls<100:
                rolls += 1
                if rng.rng(4):
                    rolled(x, rolls)
                    break
            elif rolls>=100 and rolls<200:
                rolls += 1
                if rng.rng(5):
                    rolled(x, rolls)
                    break
            elif rolls>=200 and rolls<300:
                rolls += 1
                if rng.rng(6):
                    rolled(x, rolls)
                    break
            elif rolls>=300 and rolls<500:
                rolls += 1
                if rng.rng(7):
                    rolled(x, rolls)
                    break
            elif rolls>=500:
                rolls += 1
                if rng.rng(8):
                    rolled(x, rolls)
                    break



method = input('''What gen/method would you like to roll in?
1 = gen 2-5 full odds
2 = gen 6 onwards full odds
3 = gen 8 full odds\n''')
roll(method)
while True:
    roll(input('Go again? type 1, 2 or 3 again if yes '))
