import re

list_codes = []
with open("day_1/input.txt") as my_file:
    list_codes = my_file.read().split("\n")

string_to_num_conversion = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def _replace_name_with_number(code: str) -> list:
    """
    Replace the name of a number with number
    """
    for number in string_to_num_conversion.keys():
        if number in code:
            code.replace(number, str(string_to_num_conversion.get(f"{number}")))

    return code


def _retrive_numbers(code: str) -> list:
    """
    Return a list with all the numbers of the code
    """
    numbers = []
    for character in code:
        if not character.isalpha():
            numbers.append(character)
    return numbers


def _generate_code(number_list: list) -> int:
    """
    Generate a number with the first and last number
    """
    return int(number_list[0] + number_list[-1])


def _uncyper_code_and_sum(code_list: list) -> int:
    """
    Uncyper the challlenge
    """
    numbers = []
    for code in code_list:
        code = _replace_name_with_number(code=code)
        filtred_numbers = _retrive_numbers(code=code)
        numbers.append(_generate_code(filtred_numbers))
    return sum(numbers)


print(_uncyper_code_and_sum(list_codes))
