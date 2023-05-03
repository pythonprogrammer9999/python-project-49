from random import randint

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_game():
    question = randint(1, 100)
    counter = 0
    for i in range(1, question + 1):
        if question % i == 0:
            counter += 1
    if counter == 2:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
