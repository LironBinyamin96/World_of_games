import random

def generate_number(difficulty_level):
    match difficulty_level:
        case 1:
            secret_number = random.randint(1, 3)
            return [secret_number, 1, 3]
        case 2:
            secret_number = random.randint(1, 5)
            return [secret_number, 1, 5]
        case 3:
            secret_number = random.randint(1, 10)
            return [secret_number, 1, 10]
        case 4:
            secret_number = random.randint(1, 15)
            return [secret_number, 1, 15]
        case 5:
            secret_number = random.randint(1, 20)
            return [secret_number, 1, 20]


def get_guess_from_user(min_number,max_number):
    difficulty = (input(f"Please choose a number between {min_number} and {max_number}: "))
    return difficulty


def compare_results(secret_number,difficulty):
    if secret_number == difficulty:
        return True
    return False


def play(difficulty):
    results_of_generate_number = generate_number(difficulty)
    secret_number = int(results_of_generate_number[0])
    difficulty = get_guess_from_user(int(results_of_generate_number[1]), int(results_of_generate_number[2]))
    print(f'secret_number is {secret_number}')
    print(f'difficulty is {difficulty}')
    if secret_number == difficulty:
        return True
    return False


