import random
import math


MANUAL = 'Find the greatest common divisor of given numbers.'
BEGIN_OF_RANGE = 1
END_OF_RANGE = 100


def generate_game():
    first_num = random.randint(BEGIN_OF_RANGE, END_OF_RANGE)
    second_num = random.randint(BEGIN_OF_RANGE, END_OF_RANGE)
    question = f'{first_num} {second_num}'
    answer = str(math.gcd(first_num, second_num))
    return question, answer
