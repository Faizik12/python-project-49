#!/usr/bin/env python3
import random


MANUAL = 'What number is missing in the progression?'


def create_progression():
    len_of_progression = random.randint(5, 10)
    start_of_progression = random.randint(0, 100)
    step_of_progression = random.randint(1, 10)
    end_of_progression = start_of_progression + \
        step_of_progression * len_of_progression
    progression = []
    for num in range(start_of_progression,
                     end_of_progression, step_of_progression):
        progression.append(num)
    return progression


def random_number(progression):
    index = random.randint(0, len(progression) - 1)
    correct_num = progression[index]
    progression[index] = '..'
    return correct_num


def game():
    progression = create_progression()
    answer = str(random_number(progression))
    question = ' '.join(map(str, progression))
    return question, answer
