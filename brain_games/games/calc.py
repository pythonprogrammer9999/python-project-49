from random import randint, choice
from operator import add, sub, mul

description = 'What is the result of the expression?'


def calc():
    random1, random2 = randint(0, 100), randint(0, 100)
    random_min, random_max = min(random1, random2), max(random1, random2)
    operators = {'+': add,
                 '-': sub,
                 '*': mul,
                 }
    operator = choice(list(operators.keys()))
    question = str(random_max) + operator + str(random_min)
    correct_answer = str(operators[operator](random_max, random_min))

    return question, correct_answer
