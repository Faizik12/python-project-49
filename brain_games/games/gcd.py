import random


MANUAL = 'Find the greatest common divisor of given numbers.'
BEGIN_OF_RANGE = 1
END_OF_RANGE = 100


def give_correct_answer(first_num, second_num):
    min_num = min(first_num, second_num)
    for i in range(min_num, 0, -1):
        if first_num % i == 0 and second_num % i == 0:
            return i


def generate_game():
    first_num = random.randint(BEGIN_OF_RANGE, END_OF_RANGE)
    second_num = random.randint(BEGIN_OF_RANGE, END_OF_RANGE)
    question = f'{first_num} {second_num}'
    answer = str(give_correct_answer(first_num, second_num))
    return question, answer
