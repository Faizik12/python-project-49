import random


MANUAL = 'Answer "yes" if the number is even, otherwise answer "no".'
BEGIN_OF_RANGE = 0
END_OF_RANGE = 100


def is_even(number):
    return number % 2 == 0


def generate_game():
    question = random.randint(BEGIN_OF_RANGE, END_OF_RANGE)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
