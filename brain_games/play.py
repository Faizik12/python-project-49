import prompt


ATTEMPTS = 3


def launch_game(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.MANUAL)
    for i in range(ATTEMPTS):
        question, current_answer = game_module.generate_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == current_answer:
            print('Correct!')
            continue
        print(f'\'{answer}\' is wrong answer ;(. '
              f'Correct answer was \'{current_answer}\'.')
        print(f'Let\'s try again, {name}!')
        return
    print(f'Congratulations, {name}!')
