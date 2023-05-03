from random import randint

description = 'What number is missing in the progression?'


def progression_game():
    initial, difference = randint(1, 50), randint(1, 10)
    length = randint(5, 10)
    my_list = [initial]
    for i in range(length):
        initial = initial + difference
        my_list += [initial]
    correct_answer = my_list[randint(0, length)]
    skipped = my_list.index(correct_answer)
    my_list[skipped] = '..'
    question = ' '.join(str(item) for item in my_list)
    return question, str(correct_answer)
