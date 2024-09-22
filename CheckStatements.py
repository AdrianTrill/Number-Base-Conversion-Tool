def check_if_rapid_conversion_is_available(base_1, base_2):
    # This function checks if the rapid conversion method is available for the given bases
    if base_1 == 2 and (base_2 == 4 or base_2 == 8 or base_2 == 16):
        return True

    if base_2 == 2 and (base_1 == 4 or base_1 == 8 or base_1 == 16):
        return True

    return False


def check_if_base_is_valid(base_1):
    # This function checks if the base is valid
    return (1 < base_1 < 11) or base_1 == 16


def check_if_number_is_available_in_base_b(chosen_number, base):
    # This function checks if the number is available in base b

    list_of_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    for digit in chosen_number:
        if digit not in list_of_digits:
            return False

        digit = list_of_digits.index(digit)

        if digit >= base:
            return False

    return True


def greater_numbers(first_number, second_number):
    # This function checks which number is greater and returns them in the correct order

    if len(first_number) > len(second_number):
        return first_number, second_number, ''
    if len(first_number) < len(second_number):
        return second_number, first_number, '-'
    for i in range(len(first_number)):
        if first_number[i] > second_number[i]:
            return first_number, second_number, ''
        if first_number[i] < second_number[i]:
            return second_number, first_number, '-'
    return first_number, second_number, ''
