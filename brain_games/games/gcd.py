from random import randint
from math import gcd

description = 'Find the greatest common divisor of given numbers.'


def gcd_game():
    random1, random2 = randint(1, 100), randint(1, 100)
    question = f'{str(random1)} {str(random2)}'
    correct_answer = str(gcd(random1, random2))
    return question, correct_answer
