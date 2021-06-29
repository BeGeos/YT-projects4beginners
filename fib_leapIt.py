
def fibonacci(num):
    # Fn = (Fn-1) + (Fn-2)

    # Base cases
    if num == 1:
        return 1

    if num == 0:
        return 0

    # recursive call
    return fibonacci(num - 1) + fibonacci(num - 2)


# print(fibonacci(30))


def is_leap(year):
    # Divisible by 4 or if divisible by 100 and by 400
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False


def better_is_leap(year):
    return (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)


y = 1900
print(is_leap(y))
print(better_is_leap(y))
