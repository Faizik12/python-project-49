import random


MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'
BEGIN_OF_RANGE = 2
END_OF_RANGE = 100


def is_prime(number):
    for num in range(BEGIN_OF_RANGE, (number // 2) + 1):
        if number % num == 0:
            return False
    else:
        return True


def generate_game():
    question = random.randint(BEGIN_OF_RANGE, END_OF_RANGE)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
