import random


MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'
BEGINNING_OF_RANGE = 2
END_OF_RANGE = 100


def is_prime(number):
    for num in range(BEGINNING_OF_RANGE, (number // 2) + 1):
        if number % num == 0:
            return num


def generate_a_game():
    question = random.randint(BEGINNING_OF_RANGE, END_OF_RANGE)
    answer = 'no' if is_prime(question) else 'yes'
    return question, answer
