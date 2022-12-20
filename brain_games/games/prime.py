import random


MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for num in range(2, number // 2 + 1):
        if number % num == 0:
            return num


def game():
    question = random.randint(2, 100)
    answer = 'no' if is_prime(question) else 'yes'
    return question, answer
