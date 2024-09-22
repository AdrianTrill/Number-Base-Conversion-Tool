import CheckStatements
import ConversionMethods


########
def string_to_digit(digit: str) -> int:
    # This function converts a digit from any base to base 10
    # letter G = 16 is required because of the way multiplication is implemented,
    # being able to multiply only by a digit
    digits_in_any_base = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                          'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16,
                          'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16}
    return digits_in_any_base[digit]


def digit_to_string(digit: int) -> str:
    # This function converts a digit from base 10 to any base
    digits_in_base_10 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                         10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G'}
    return digits_in_base_10[digit]


def add_two_digits(digit_1: str, digit_2: str, base: int, carry: int = 0) -> tuple[str, int]:
    digit_1 = string_to_digit(digit_1)
    digit_2 = string_to_digit(digit_2)

    if carry + digit_1 + digit_2 >= base:    # checks if there will be a carry and if not, adds the digits
        sum_of_digits = carry + digit_1 + digit_2 - base
        carry = 1
    else:
        sum_of_digits = carry + digit_1 + digit_2
        carry = 0

    return digit_to_string(sum_of_digits), carry


def subtract_two_digits(digit_1: str, digit_2: str, base: int, carry: int = 0) -> tuple[str, int]:
    # checks if the first digit is greater than the second one and if not, swaps them
    # (this is done to avoid negative numbers)
    minuend = string_to_digit(digit_1)
    subtrahend = string_to_digit(digit_2)

    if carry + minuend - subtrahend < 0:  # checks if there will be a carry
        difference = carry + minuend - subtrahend + base
        carry = -1
    else:
        difference = carry + minuend - subtrahend
        carry = 0

    return digit_to_string(difference), carry


def multiply_two_digits(digit_1: str, digit_2: str, base: int, carry: int = 0) -> tuple[str, int]:
    digit_1 = string_to_digit(digit_1)
    digit_2 = string_to_digit(digit_2)

    # checks if there will be a carry
    if carry + digit_1 * digit_2 >= base:
        product = (carry + digit_1 * digit_2) % base
        carry = (carry + digit_1 * digit_2) // base
    else:
        product = carry + digit_1 * digit_2
        carry = 0

    return digit_to_string(product), carry


def equalize_lengths(number_1: str, number_2: str) -> tuple[str, str]:
    # checks if the numbers have the same length and if not, adds zeroes to the start of the shorter one
    if len(number_1) > len(number_2):  # adds zeroes to number_2 if necessary
        string_of_zeroes = ''
        difference_in_length = len(number_1) - len(number_2)
        for _ in range(difference_in_length):
            string_of_zeroes += '0'
        number_2 = string_of_zeroes + number_2

    elif len(number_2) > len(number_1):  # adds zeroes to number_1 if necessary
        string_of_zeroes = ''
        difference_in_length = len(number_2) - len(number_1)
        for _ in range(difference_in_length):
            string_of_zeroes += '0'
        number_1 = string_of_zeroes + number_1

    return number_1, number_2


def add_two_numbers(number_1: str, number_2: str, base: int) -> str:
    sum_of_numbers = ''
    carry = 0

    number_1, number_2 = equalize_lengths(number_1, number_2)
    index = len(number_1) - 1

    while index >= 0:
        sum_of_digits, carry = add_two_digits(number_1[index], number_2[index], base, carry)
        sum_of_numbers = sum_of_digits + sum_of_numbers
        index -= 1
    # checks if we have a leftover carry outside the numbers maximum length
    if carry != 0:
        sum_of_numbers = digit_to_string(carry) + sum_of_numbers

    return sum_of_numbers


def subtract_two_numbers(number_1: str, number_2: str, base: int) -> str:
    # checks if the first number is greater than the second one and if not, swaps them
    negative = False
    if int(ConversionMethods.convert_using_successive_divisions_method(number_1, base, 10)) < int(ConversionMethods.convert_using_successive_divisions_method(number_2, base, 10)):
        number_2, number_1 = number_1, number_2
        negative = True

    difference = ''
    carry = 0

    number_1, number_2 = equalize_lengths(number_1, number_2)
    index = len(number_1) - 1

    while index >= 0:
        difference_of_digits, carry = subtract_two_digits(number_1[index], number_2[index], base, carry)
        difference = difference_of_digits + difference
        index -= 1
    # removes unnecessary zeroes at the start of the difference
    while difference[0] == '0':
        if difference == '0':
            break
        difference = difference[1:]
    # checks if the difference is negative and adds a minus sign
    if negative:
        difference = '-' + difference

    return difference


def multiply_number_by_a_digit(number: str, digit: str, base: int) -> str:
    product = ''
    carry = 0

    index = len(number) - 1

    while index >= 0:
        product_digits, carry = multiply_two_digits(number[index], digit, base, carry)
        product = product_digits + product
        index -= 1
    # checks if we have a leftover carry outside the numbers maximum length
    if carry != 0:
        product = digit_to_string(carry) + product

    if product == "0" * len(product):
        product = "0"

    return product


def divide_number_by_a_digit(number: str, digit: str, base: int) -> tuple[str, str]:
    quotient = ''
    remainder = ''

    number = '0' + number  # add a zero to the start of the number

    while not len(number) == 1 or not string_to_digit(number[0]) < string_to_digit(digit):
        first_two_digits_in_base_10 = string_to_digit(number[0]) * base + string_to_digit(number[1])

        quotient = quotient + digit_to_string(first_two_digits_in_base_10 // string_to_digit(digit))
        remainder = digit_to_string(first_two_digits_in_base_10 % string_to_digit(digit))

        number = remainder + number[2:]

    # We remove the unnecessary zeroes from our result if they are present
    while quotient[0] == '0':
        if quotient == '0':
            break
        quotient = quotient[1:]

    return quotient, remainder



