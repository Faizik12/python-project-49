import random


MANUAL = 'What is the result of the expression?'
BEGINNING_OF_RANGE = 0
END_OF_RANGE = 100
OPERATORS = ['+', '-', '*']
DELIMITER = ' '


def give_the_correct_answer(operations):
    list_of_elements = operations.split(DELIMITER)
    if list_of_elements[1] == '+':
        return int(list_of_elements[0]) + int(list_of_elements[2])
    if list_of_elements[1] == '-':
        return int(list_of_elements[0]) - int(list_of_elements[2])
    return int(list_of_elements[0]) * int(list_of_elements[2])


def select_an_operator():
    return random.choice(OPERATORS)


def generate_a_game():
    first_num = random.randint(BEGINNING_OF_RANGE, END_OF_RANGE)
    second_num = random.randint(BEGINNING_OF_RANGE, END_OF_RANGE)
    operator = select_an_operator()
    question = f'{first_num} {operator} {second_num}'
    answer = str(give_the_correct_answer(question))
    return question, answer
