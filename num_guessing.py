import random


# Helper functions
def is_even(num):
    if num % 2 == 0:
        return "It's even"
    return "It's odd"


def is_prime(num):
    for number in range(2, (num // 2) +1):
        if num % number == 0:
            return "It's not a prime number"
    return "It's a prime number"


dividers_bin = []


def is_divisible_by(num):
    counter = 0
    while counter < 20:
        divider = random.randint(3, (num // 2) - 1)
        if num % divider == 0 and divider not in dividers_bin:
            dividers_bin.append(divider)
            return f"It's divisible by {divider}"
        counter += 1
    return "It doesn't have many dividers"


helper_functions = [is_even, is_prime, is_divisible_by]


def help_user(num):
    which = random.choice(helper_functions)
    help_text = which(num)
    if helper_functions.index(which) != 2:
        helper_functions.remove(which)
    return help_text


def game():
    score = 100
    remainder = 0
    num = random.randint(1, 100)

    while score > 0:
        guess = input("What's the number?\n")
        random_divider = random.randint(2, 9)
        if remainder != 0 and remainder % random_divider == 0:
            print(help_user(num))
            score -= 2
        try:
            guess = int(guess)
        except ValueError:
            print("That's not a valid number")
            continue

        if guess == num:
            print(f"You win! and this is the score {score}")
            return
        elif guess < num:
            score -= 10
            remainder += 10
            print("Too low!")
        elif guess > num:
            score -= 10
            remainder += 10
            print("Too high!")

    print(f"Sorry you lost! the number is {num}")


if __name__ == "__main__":
    game()
