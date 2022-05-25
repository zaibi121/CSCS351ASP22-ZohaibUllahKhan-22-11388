def take_power(num1, num2):
    return (num1 ** num2)


def palindrome(my_str):

    my_str = my_str.casefold()

    rev_str = reversed(my_str)

    if list(my_str) == list(rev_str):
        return True
    else:
        return False
