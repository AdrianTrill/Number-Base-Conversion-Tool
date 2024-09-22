import math
import NumberBaseOperations


def rapid_conversion_from_base_2(base_two_number, target_base):
    # Correspondence table is a python dictionary, that has all the equivalent representations for the numbers from 0 to 16 in their corresponding base
    corresponding_number_representation_table = {
        2: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"],
        4: ["0", "1", "2", "3", "10", "11", "12", "13", "20", "21", "22", "23", "30", "31", "32", "33"],
        8: ["0", "1", "2", "3", "4", "5", "6", "7", "10", "11", "12", "13", "14", "15", "16", "17"],
        16: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"],
    }

    index_base_two_number = len(base_two_number) - 1
    grouped_digits = int(math.log(target_base, 2))

    result = ""

    while index_base_two_number >= 0:
        # We take the digits from the base 2 number, from right to left, and we group them in groups of grouped_digits digits
        group = ""

        for _ in range(grouped_digits):
            # We add the digits to the group, as long as we have digits to add
            if index_base_two_number >= 0:
                group = base_two_number[index_base_two_number] + group
                index_base_two_number -= 1
        # We add 0 at the front of the group, as long as the group has fewer digits than grouped_digits
        while group[0] == '0' and len(group) > 1:
            group = group[1:]

        # We find the equivalent representation of the group in the target base, and we add it at the front of the result
        result = corresponding_number_representation_table[target_base][corresponding_number_representation_table[2].index(group)] + result

    return result


def rapid_conversion_to_base_2(number_in_base, from_base_convert):
    # Correspondence table is a python dictionary, that has all the equivalent representations for the numbers from 0 to 16 in their corresponding base
    correspondence_table = {
        2: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"],
        4: ["0", "1", "2", "3", "10", "11", "12", "13", "20", "21", "22", "23", "30", "31", "32", "33"],
        8: ["0", "1", "2", "3", "4", "5", "6", "7", "10", "11", "12", "13", "14", "15", "16", "17"],
        16: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"],
    }

    # grouped_digits represent how many digits are in base 2 from base p in a group
    # Example: For converting from base 16, a digit in base 16 corresponds to 4 digits in base 2

    grouped_digits = int(math.log(from_base_convert, 2))
    index_number_in_base = len(number_in_base) - 1

    result = ""

    while index_number_in_base >= 0:
        # We loop inside our number, from left to right. As we take a digit, we find the equivalent representation in base 2
        group = correspondence_table[2][correspondence_table[from_base_convert].index(str(number_in_base[index_number_in_base]))]
        index_number_in_base -= 1
        # We add 0 at the front of the group, as long as the group has fewer digits than grouped_digits
        while len(group) < grouped_digits:
            group = "0" + group

        result = group + result

    # We remove the leading zeroes from our result if they are present
    while len(result) > 1 and result[0] == '0':
        result = result[1:]

    return result


def convert_using_substitution_method(converting_number, source_base, destination_base):
    list_of_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

    # We find the equivalent of our base in our digit representation
    source_base = list_of_digits[source_base]

    index = len(converting_number) - 1

    res = ""
    multiplier_number = "1"

    while index >= 0:
        # We take the digits from the number, from right to left, and we multiply them with the multiplier_number
        # The result is added to the final result
        # The multiplier_number is multiplied with the source_base
        digit = converting_number[index]
        current_number = NumberBaseOperations.multiply_number_by_a_digit(multiplier_number, digit, destination_base)
        res = NumberBaseOperations.add_two_numbers(res, current_number, destination_base)
        multiplier_number = NumberBaseOperations.multiply_number_by_a_digit(multiplier_number, source_base, destination_base)
        index -= 1

    # We remove the leading zeroes from our result if they are present
    while len(res) > 0 and res[0] == '0':
        res = res[1:]

    return res


def convert_using_successive_divisions_method(converting_number, source_base, destination_base):
    list_of_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

    # We find the equivalent of our base in our digit representation
    source_base = list_of_digits[source_base]

    res = ""
    #
    while converting_number != "0":
        # We divide the number by the destination_base, and we find the remainder
        # The remainder is added at the front of the result
        # The number is updated with the result of the division
        converting_number, remainder = NumberBaseOperations.divide_number_by_a_digit(converting_number, source_base, destination_base)
        res = list_of_digits[int(remainder)] + res

    # We remove the leading zeroes from our result if they are present
    while len(res) > 0 and res[0] == '0':
        res = res[1:]

    return res


def convert_using_base_10_as_intermediary_base(converting_number, source_base, destination_base):
    # We convert the number from the source_base to base 10
    # We convert the number from base 10 to the destination_base
    # We return the result

    result_in_base_10 = convert_using_substitution_method(converting_number, source_base, 10)
    return result_in_base_10, convert_using_substitution_method(result_in_base_10, 10, destination_base)

