#!/usr/bin/evn python3
import prompt


ATTEMPTS = 3


def game_progress(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.TEST)
    for i in range(ATTEMPTS):
        question, current_answer = game_module.game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == current_answer:
            print('Correct!')
            continue
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{current_answer}'.")
        print(f"Let's try again, {name}")
        return
    print(f'Congratulations, {name}!')
    