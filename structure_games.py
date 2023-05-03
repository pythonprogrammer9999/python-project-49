import prompt


def structute(even, description):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(description)
    for counter in range(3):
        question, correct_answer = even()
        print('Question:', question)
        user_answer = prompt.string('Your answer:')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"{user_answer} is wrong answer ;(.\\"
                f" Correct answer was '{correct_answer}'.\
                \nLet's try again, {name}!)")
            exit()
    print(f'Congratulations, {name}!')
