from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    random_nomber = randint(0, 100)
    question = random_nomber
    if random_nomber % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
