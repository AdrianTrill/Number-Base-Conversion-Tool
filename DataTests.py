import ConversionMethods
import NumberBaseOperations


def test_convert_using_substitution_method():
    assert ConversionMethods.convert_using_substitution_method("1010", 2, 10) == "10"
    assert ConversionMethods.convert_using_substitution_method('10001101', 2, 7) == '261'
    assert ConversionMethods.convert_using_substitution_method('24213433034122404', 5, 12) == '71713417456'


def test_convert_using_successive_divisions_method():
    assert ConversionMethods.convert_using_successive_divisions_method("10", 10, 2) == "1010"
    assert ConversionMethods.convert_using_successive_divisions_method('10001101', 2, 7) == '261'
    assert ConversionMethods.convert_using_successive_divisions_method('71713417456', 12, 5) == '24213433034122404'


def test_add_two_numbers():
    assert NumberBaseOperations.add_two_numbers("1010", "1010", 2) == "10100"
    assert NumberBaseOperations.add_two_numbers('76', '90A', 11) == '985'
    assert NumberBaseOperations.add_two_numbers('7C', '97', 15) == '124'


def test_subtract_two_numbers():
    assert NumberBaseOperations.subtract_two_numbers("1010", "1010", 2) == "0"
    assert NumberBaseOperations.subtract_two_numbers("1B23", "97", 15) == "1A7B"


def test_multiply_number_by_a_digit():
    assert NumberBaseOperations.multiply_number_by_a_digit("1010", "1", 2) == "1010"
    assert NumberBaseOperations.multiply_number_by_a_digit("53", "4", 6) == "340"
    assert NumberBaseOperations.multiply_number_by_a_digit("53A", "7", 12) == "312A"


def test_divide_number_by_a_digit():
    assert NumberBaseOperations.divide_number_by_a_digit("1010", "1010", 2) == ("1", "0")
    assert NumberBaseOperations.divide_number_by_a_digit('67ABC56', 'A', 13) == ('877907', '1')


def test_rapid_conversion_from_base_2():
    assert ConversionMethods.rapid_conversion_from_base_2("1010", 16) == "A"
    assert ConversionMethods.rapid_conversion_from_base_2("1010", 8) == "12"
    assert ConversionMethods.rapid_conversion_from_base_2("1010", 4) == "22"


def test_rapid_conversion_to_base_2():
    assert ConversionMethods.rapid_conversion_to_base_2('A', 16) == '1010'
    assert ConversionMethods.rapid_conversion_to_base_2('72', 8) == '111010'


def test_convert_using_base_10_as_intermediary_base():
    assert ConversionMethods.convert_using_base_10_as_intermediary_base('10001101', 2, 7) == '261'
    assert ConversionMethods.convert_using_base_10_as_intermediary_base('24213433034122404', 5, 12) == '71713417456'


def test_all_functions():
    test_convert_using_substitution_method()
    test_convert_using_successive_divisions_method()
    test_add_two_numbers()
    test_subtract_two_numbers()
    test_multiply_number_by_a_digit()
    test_divide_number_by_a_digit()
    test_rapid_conversion_from_base_2()
    test_rapid_conversion_to_base_2()
    test_convert_using_base_10_as_intermediary_base()
