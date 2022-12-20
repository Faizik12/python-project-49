import random


MANUAL = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def game():
    question = random.randint(0, 100)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
