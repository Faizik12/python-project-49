#!/usr/bin/env python3
import random


MANUAL = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def what_answer(operations):
    return eval(operations)


def what_operator():
    return random.choice(OPERATORS)


def game():
    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)
    question = f'{first_num} {what_operator()} {second_num}'
    answer = str(what_answer(question))
    return question, answer
