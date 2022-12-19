#!/usr/bin/env python3
import random


MANUAL = 'Find the greatest common divisor of given numbers.'

def what_answer(first_num, second_num):
    min_num = min(first_num, second_num)
    for i in range(min_num, 0, -1):
        if first_num % i == 0 and second_num % i == 0:
            return i


def game():
    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)
    question = f'{first_num} {second_num}'
    answer = str(what_answer(first_num, second_num))
    return question, answer
