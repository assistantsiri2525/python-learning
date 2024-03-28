import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def difficulty_level(level):
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return


def compare_answer(user_guess_number, answer, total_attempts):
    if user_guess_number < answer:
        print('number is too low')
        return total_attempts - 1
    elif user_guess_number > answer:
        print('number is too high')
        return total_attempts - 1
    else:
        print(f'Your answer is correct..That is {answer}')


def game_world():
    print('Let me think the number between 1 to 50')
    answer = random.randint(1, 50)

    level_of_difficulty = input('choose level of difficulty... easy or hard: ')
    total_attempts = difficulty_level(level_of_difficulty)

    user_guess_number = 0
    while user_guess_number != answer:
        print(f'Given {total_attempts} to guess the number')

        user_guess_number = int(input("Please guess the number: "))
        total_attempts = compare_answer(user_guess_number, answer, total_attempts)
        if total_attempts == 0:
            print('All attempts exhausted...start again')
            exit()
        elif user_guess_number != answer:
            print('guess again')


if __name__ == '__main__':
    game_world()
