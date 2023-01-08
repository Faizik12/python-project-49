import random


MANUAL = 'What number is missing in the progression?'
MINIMUM_LENGTH = 5
MAXIMUM_LENGTH = 10
MINIMUM_STEP = 1
MAXIMUM_STEP = 10
BEGIN_OF_RANGE = 0
END_OF_RANGE = 100


def create_progression():
    len_of_progression = random.randint(MINIMUM_LENGTH, MAXIMUM_LENGTH)
    start_of_progression = random.randint(BEGIN_OF_RANGE, END_OF_RANGE)
    step_of_progression = random.randint(MINIMUM_STEP, MAXIMUM_STEP)
    end_of_progression = start_of_progression + \
        step_of_progression * len_of_progression
    progression = []
    for num in range(start_of_progression,
                     end_of_progression, step_of_progression):
        progression.append(num)
    return progression


def choose_random_number(progression):
    index = random.randint(BEGIN_OF_RANGE, len(progression) - 1)
    correct_num = progression[index]
    progression[index] = '..'
    return correct_num


def generate_game():
    progression = create_progression()
    answer = str(choose_random_number(progression))
    question = ' '.join(map(str, progression))
    return question, answer
