import random


MANUAL = 'What is the result of the expression?'
BEGIN_OF_RANGE = 0
END_OF_RANGE = 100
OPERATORS = ['+', '-', '*']
DELIMITER = ' '


def give_correct_answer(first_number, operator, second_number):
    if operator == '+':
        return first_number + second_number
    if operator == '-':
        return first_number - second_number
    if operator == '*':
        return first_number * second_number


def generate_game():
    first_num = random.randint(BEGIN_OF_RANGE, END_OF_RANGE)
    second_num = random.randint(BEGIN_OF_RANGE, END_OF_RANGE)
    operator = random.choice(OPERATORS)
    question = f'{first_num} {operator} {second_num}'
    answer = str(give_correct_answer(question))
    return question, answer
