import time
import random


def generate_sequence(difficulty_level):
    match difficulty_level:
        case 1:
            list_numbers = [random.randint(1, 101) for _ in range(difficulty_level)]
            return [list_numbers, difficulty_level]
        case 2:
            list_numbers = [random.randint(1, 101) for _ in range(difficulty_level)]
            return [list_numbers, difficulty_level]
        case 3:
            list_numbers = [random.randint(1, 101) for _ in range(difficulty_level)]
            return [list_numbers, difficulty_level]
        case 4:
            list_numbers = [random.randint(1, 101) for _ in range(difficulty_level)]
            return [list_numbers, difficulty_level]
        case 5:
            list_numbers = [random.randint(1, 101) for _ in range(difficulty_level)]
            return [list_numbers, difficulty_level]


def get_list_from_user(num_for_range):
    print("Please write a number that you remember separated by spaces")
    list_from_user = []
    for i in range(num_for_range):
        user_input = input(f"Enter number {i + 1}: ")
        if user_input.isdigit():
            number = int(user_input)
            list_from_user.append(number)
    return list_from_user


def is_list_equal(generate_list, user_lise):
    if generate_list == user_lise:
        return True
    return False


def play(difficulty):
    temp_generate_list = generate_sequence(difficulty)
    print(temp_generate_list[0])
    time.sleep(0.7)
    print('\n' * 50)
    temp_user_list = get_list_from_user(temp_generate_list[1])
    print(is_list_equal(temp_generate_list[0], temp_user_list))

