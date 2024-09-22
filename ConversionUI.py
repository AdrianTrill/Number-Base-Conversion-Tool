import ConversionMethods
import CheckStatements
import NumberBaseOperations


def print_ui():
    print("Author of this project: Mititean Adrian")
    while True:
        print("Enter the index of the task you want to perform:")
        print("1. Convert a number from a base to another")
        print("2. Perform operations on numbers in a chosen base")
        print("3. Exit 402-404")

        option = int(input("Select an option: "))

        if option == 1:
            print("Conversion methods available below please enter the number for the corresponding method you want to use:")
            print("1. Convert using base 10 as an intermediary base")
            print("2. Convert using rapid conversions")
            print("3. Convert using substitution method")
            print("4. Convert using successive divisions method")

            option = int(input("Select an option: "))
            converting_number = input("Number you want to convert ").upper()
            source_base = int(input("Base you want to convert from "))
            destination_base = int(input("Destination base "))

            if option == 1:
                if CheckStatements.check_if_base_is_valid(source_base) and CheckStatements.check_if_base_is_valid(destination_base) and CheckStatements.check_if_number_is_available_in_base_b(converting_number, source_base):
                    nr_in_10, nr_in_h = ConversionMethods.convert_using_base_10_as_intermediary_base(converting_number, source_base, destination_base)
                    print(f"The number {converting_number} in base {source_base} is {nr_in_10} in base 10")
                    print(f"The number {nr_in_10} in base 10 is {nr_in_h} in base {destination_base}")
                else:
                    print("Invalid Input! Please try again :)")

            elif option == 2:
                if CheckStatements.check_if_base_is_valid(source_base) and CheckStatements.check_if_base_is_valid(destination_base) and CheckStatements.check_if_rapid_conversion_is_available(source_base,
                                                                                                                                                    destination_base) and CheckStatements.check_if_number_is_available_in_base_b(
                        converting_number, source_base):
                    if source_base == 2:
                        res = ConversionMethods.rapid_conversion_from_base_2(converting_number, destination_base)
                    else:
                        res = ConversionMethods.rapid_conversion_to_base_2(converting_number, source_base)
                    print(f"The number {converting_number} in base {source_base} is {res} in base {destination_base}")
                else:
                    print("Invalid Input! Please try again :)")

            elif option == 3:
                print("For this method, the source base has to be smaller than the destination base. Try again")
                if CheckStatements.check_if_base_is_valid(source_base) and CheckStatements.check_if_base_is_valid(destination_base) and source_base < destination_base and CheckStatements.check_if_number_is_available_in_base_b(converting_number, source_base):
                    res = ConversionMethods.convert_using_substitution_method(converting_number, source_base, destination_base)
                    print(f"The number {converting_number} in base {source_base} is {res} in base {destination_base}")
                else:
                    print("Invalid Input! Please try again :)")

            elif option == 4:
                print("For this method, the source base has to be greater than the destination base. Try again")
                if CheckStatements.check_if_base_is_valid(source_base) and CheckStatements.check_if_base_is_valid(destination_base) and source_base > destination_base and CheckStatements.check_if_number_is_available_in_base_b(converting_number, source_base):
                    res = ConversionMethods.convert_using_successive_divisions_method(converting_number, destination_base, source_base)
                    print(f"The number {converting_number} in base {source_base} is {res} in base {destination_base}")
                else:
                    print("Invalid Input! Please try again :)")

            else:
                print("Your input does not match any of the available options from above. Try again")

        elif option == 2:
            print("Number Base Operations available. Please enter the corresponding number for the operation you want to perform:")
            print("1. Add 2 numbers in a chosen base")
            print("2. Subtract 2 numbers in a chosen base")
            print("3. Multiply a number to a digit in a chosen base")
            print("4. Divide a number to a digit in a chosen base")

            option = int(input("Select an option: "))

            source_base = int(input("Choose your desired base "))
            first_number = input("Enter the first number ").upper()
            generate_number = input("Enter the second number ").upper()

            if option == 1:
                if CheckStatements.check_if_base_is_valid(source_base) and CheckStatements.check_if_number_is_available_in_base_b(first_number, source_base) and CheckStatements.check_if_number_is_available_in_base_b(generate_number, source_base):
                    res = NumberBaseOperations.add_two_numbers(first_number, generate_number, source_base)
                    print(f"{first_number}+{generate_number} in base {source_base} is equal to {res}")
                else:
                    print("Invalid Input! Please try again :)")

            elif option == 2:
                if CheckStatements.check_if_base_is_valid(source_base) and CheckStatements.check_if_number_is_available_in_base_b(first_number, source_base) and CheckStatements.check_if_number_is_available_in_base_b(generate_number, source_base):
                    res = NumberBaseOperations.subtract_two_numbers(first_number, generate_number, source_base)
                    print(f"{first_number}-{generate_number} in base {source_base} is equal to {res}")
                else:
                    print("Invalid Input! Please try again :)")

            elif option == 3:
                if len(generate_number) == 1 and CheckStatements.check_if_base_is_valid(source_base) and CheckStatements.check_if_number_is_available_in_base_b(first_number, source_base) and CheckStatements.check_if_number_is_available_in_base_b(
                        generate_number, source_base):
                    res = NumberBaseOperations.multiply_number_by_a_digit(first_number, generate_number, source_base)
                    print(f"{first_number} * {generate_number} in base {source_base} is equal to {res}")
                else:
                    print("Invalid Input! Please try again :)")

            elif option == 4:
                if len(generate_number) == 1 and CheckStatements.check_if_base_is_valid(source_base) and CheckStatements.check_if_number_is_available_in_base_b(first_number, source_base) and CheckStatements.check_if_number_is_available_in_base_b(
                        generate_number, source_base):
                    res, remainder = NumberBaseOperations.divide_number_by_a_digit(first_number, generate_number, source_base)
                    print(f"{first_number}/{generate_number} in base {source_base} is equal to {res}")
                    print(f"The remainder of this operation is {remainder}")
                else:
                    print("Invalid Input! Please try again :)")

            else:
                print("Your input does not match any of the available options from above. Please try again")
        elif option == 3:
            print("Sayonara!!")
            return

        option = input("Do you want to continue performing other tasks? (yes or no) [Y/N]").upper()
        if option == "N":
            print("Sayonara!!")
            return
