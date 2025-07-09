""" Translator class for managing a knowledge base of products and their prices."""

import os
import pickle

from Solution1.TranslatorExceptions import ForeignNumberException


def add_entry(dictionary: dict, key, value, entry_type: str = "dictionary"):
    if key in dictionary and dictionary[key] != value:
        old_value = dictionary[key]
        print(f"Overwriting '{key}' with '{value}' (was '{old_value}') in {entry_type}")
    elif key in dictionary and dictionary[key] == value:
        print(f"'{key}' with '{value}' already exists in {entry_type}")
        return
    else:
        print(f"Adding new {entry_type} '{key}' with '{value}'")
    dictionary[key] = value


class Translator:
    def __init__(self, backup_path: str = r"./backup.pkl", roman_numbers: dict = None):
        self.knowledge_base = {}
        self.foreign_numbers = {}
        self.backup_path = backup_path
        self.roman_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        } if roman_numbers is None else roman_numbers

    def roman_to_int(self, number: str):
        return self.roman_numbers[number]

    def foreign_to_roman(self, number: str):
        return self.foreign_numbers[number]

    def calc_foreign_numbers(self, values: list[str]) -> int:
        """
        Calculate the total value of foreign numbers by converting them to Roman numerals and then to integers.
        :param values: List of foreign number strings.
        :return: Integer value of the foreign numbers.
        """
        digits = []
        # translate foreign numbers to arabic digits
        for value in values:
            number = self.roman_to_int(self.foreign_to_roman(value))
            digits.append(number)

        resu = 0
        i = 0
        while i < len(digits):
            if i + 1 < len(digits) and digits[i] < digits[i + 1]:
                resu += digits[i + 1] - digits[i]
                i += 2
            else:
                resu += digits[i]
                i += 1
        return resu

    def add_foreign_number(self, new_number: str, roman_number: str):
        """
        Add a new foreign number and its corresponding Roman numeral to the knowledge base.
        :param new_number: Number in foreign language.
        :param roman_number: Roman numeral representation of the foreign number.
        """
        add_entry(self.foreign_numbers, new_number, roman_number, entry_type="foreign numbers")

    def add_knowledge_base(self, product: str, coins: float):
        """
        Add a new product and its price in coins to the knowledge base.
        :param product: Product name.
        :param coins: Price of the product in coins.
        """
        add_entry(self.knowledge_base, product, coins, entry_type="knowledge base")

    def clear_knowledge_base(self):
        self.knowledge_base = {}

    def clear_foreign_numbers(self):
        self.foreign_numbers = {}

    def delete_backup(self):
        os.remove(self.backup_path)

    def get_product_price(self, product: str) -> float:
        return self.knowledge_base[product]

    def extract_all_foreign_numbers(self, values: list[str]):
        """
        Extract all foreign numbers from the given list of values.
        :param values: List of strings. It Should contain only known foreign numbers.
        :return: Filtered list with only foreign numbers.
        :raises ForeignNumberException: If a value is not a known foreign number.
        """
        all_foreign_numbers = []
        for value in values:
            if value in self.foreign_numbers:
                all_foreign_numbers.append(value)
            else:
                raise ForeignNumberException(value)

        return all_foreign_numbers

    def save_data(self):
        """Save the current knowledge base and foreign numbers to a pickle file."""

        def save_pickle(obj, filepath: str):
            """Save an object to a pickle file."""
            with open(filepath, 'wb') as f:
                pickle.dump(obj, f)

        backup = [self.knowledge_base, self.foreign_numbers]
        save_pickle(backup, self.backup_path)

    def load_data(self):
        """Load the knowledge base and foreign numbers from a pickle file."""

        def load_pickle(filepath: str):
            """Load and return an object from a pickle file."""
            if not os.path.exists(filepath):
                return [{}, {}]

            with open(filepath, 'rb') as f:
                return pickle.load(f)

        self.knowledge_base, self.foreign_numbers = load_pickle(self.backup_path)

    def get_knowledge_base(self):
        return self.knowledge_base

    def get_foreign_numbers(self):
        return self.foreign_numbers
