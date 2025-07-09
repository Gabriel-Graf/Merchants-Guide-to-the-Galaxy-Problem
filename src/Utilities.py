""" Utilities module for the translator application."""

import re

from Solution1.TranslatorExceptions import ProductException


def extract_product_name(values: list[str]):
    """
    Extracts the product name from a list of words.
    :param values: Input list of words, which should contain the product name.
    :return: Product name as a string.
    """
    # Check if the input is a question
    if "?" in values:
        return values[values.index("?") - 1]

    try:
        is_index = values.index("is")
    except ValueError:
        raise ProductException("'is' not found in input")

    if is_index < 2:
        raise ProductException("No product name found")

    return values[is_index - 1]


def remove_keywords(words, keywords):
    """
    Removes specified keywords from a list of words.
    :param words: Input list of words.
    :param keywords: Words to be removed from the input list.
    :return: Filtered list of words without the specified keywords.
    """
    return [w for w in words if w not in keywords]


def print_error():
    """Prints an error message when the input is not recognized."""
    print("I have no idea what you are talking about")


def is_roman(s: str) -> bool:
    """
    Checks if the given string is a valid Roman numeral.
    :param s: The string to check. Should be a Roman numeral.
    :return: True if the string is a valid Roman numeral, False otherwise.
    """
    if not s:
        return False
    _ROMAN_PATTERN = re.compile(
        r'^M{0,3}(CM|CD|D?C{0,3})'
        r'(XC|XL|L?X{0,3})'
        r'(IX|IV|V?I{0,3})$'
    )

    return bool(_ROMAN_PATTERN.fullmatch(s))


def extract_digit(values: list[str]):
    """
    Extracts the first number from a list of strings. If no number is found, it raises a ValueError.
    :param values: Input list of strings, which should contain only one number.
    :return: The first number found in the list as an integer.
    :raises ValueError: If no number is found in the input list.
    """
    for value in values:
        if value.isdigit():
            return int(value)

    raise ValueError("No Number specified")


def contains_digits(values: list[str]):
    """
    Tests if the given list has numbers in it. This is useful to determine if an input is an exchange assignment or not.
    :param values: A list of strings
    :return: true if the input has at least one number as an element
    """
    for value in values:
        if value.isdigit():
            return True

    return False
