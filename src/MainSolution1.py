""" Main module for the translator application, handling user inputs and commands. """

from Solution1.CommandHandlers import ExitCommand, PrintCommand, ClearCommand, ResetCommand, HelpCommand, SaveCommand, \
    LoadCommand
from Solution1.TranslatorExceptions import ProductException, ForeignNumberException
from Solution1.Translator import Translator
from Solution1.Utilities import print_error, is_roman, extract_digit, remove_keywords, contains_digits, \
    extract_product_name


def is_command(inputs, command_map):
    """
    Checks if the first input is a valid command by comparing it with the keys in the command map.
    :param inputs: Input list of strings, where the first element is expected to be a command.
    :param command_map: Map of valid commands to their respective handler classes.
    :return: True if the first input is a valid command, False otherwise.
    """
    return inputs[0].lower() in command_map.keys()


def handle_command(inputs, translator, command_map):
    """
    Handles the command by looking it up in the command map and executing the corresponding handler.
    :param inputs: Input list of strings, where the first element is expected to be a command.
    :param translator: Translator instance to handle the command logic.
    :param command_map: Map of valid commands to their respective handler classes.
    """
    command = inputs[0].lower()
    if command in command_map:
        handler = command_map[command]
        handler.handle(inputs, translator)
    else:
        print_error()


def is_assignment(inputs):
    """
    Checks if the input is an assignment by verifying that it contains no digits and has exactly three elements.
    For example, "unu is I".
    :param inputs: Input list of strings.
    :return: True if the input is an assignment, False otherwise.
    """
    return not contains_digits(inputs) and len(inputs) == 3


def handle_assignment(inputs, translator):
    translator.add_foreign_number(inputs[0], inputs[-1])


def is_product_price_definition(inputs):
    """
    Checks if the input is a product price definition by verifying that it contains one digit and the word "coins".
    For example, "unu unu Silver is 34 coins".
    :param inputs: Input list of strings.
    :return: True if the input is a product price definition, False otherwise.
    """
    return contains_digits(inputs) and "coins" in inputs


def handle_product_price_definition(inputs, translator):
    """
    Handles the product price definition by extracting the coin value, product name, and foreign numbers from the input.
    :param inputs: Input list of strings, which should contain a product name, foreign numbers and a coin value.
    :param translator: Translator instance to handle the product price logic.
    :raises ValueError: If no number is found in the input.
    :raises ProductException: If no product name is found in the input.
    :raises ForeignNumberException: If an unknown foreign number is encountered in the input.
    """
    try:
        # Extract the coin value, product name and foreign numbers from the input
        coin_value = extract_digit(inputs)
        product_name = extract_product_name(inputs)
        filtered_inputs = remove_keywords(inputs, {product_name, str(coin_value), 'coins', 'is'})
        all_foreign_numbers = translator.extract_all_foreign_numbers(filtered_inputs)

        price = translator.calc_foreign_numbers(all_foreign_numbers)
        product_price_per_unit = coin_value / price
        translator.add_knowledge_base(product_name, product_price_per_unit)
    except ValueError as e:
        print(e)
        return
    except ProductException as e:
        print(e)
        return
    except ForeignNumberException as e:
        print(f"Unknown foreign number: {e}")
        return


def is_foreign_question(inputs: list[str]) -> bool:
    """
    Checks if the input is a foreign question by verifying that it starts with "how much is" and ends with a question mark.
    For example, "how much is dek kvindek unu unu ?".
    :param inputs: Input list of strings.
    :return: True if the input is a foreign question, False otherwise.
    """
    return (
            len(inputs) >= 4 and  # at least 4 words are needed
            inputs[0].lower() == "how" and
            inputs[1].lower() == "much" and
            inputs[2].lower() == "is" and
            inputs[-1] == "?" and
            not any(char.isdigit() for char in ' '.join(inputs))
    )


def handle_foreign_question(inputs: list[str], translator):
    """
    Handles the foreign question by translating the foreign numbers to Roman numerals and calculating their value.
    :param inputs: Input list of strings, which should contain foreign numbers and end with a question mark.
    :param translator: Translator instance to handle the foreign number logic.
    :raises KeyError: If an unknown foreign number is encountered in the input.
    :raises ForeignNumberException: If an unknown foreign number is encountered in the input.
    """
    try:
        filtered_inputs = remove_keywords(inputs, {'how', 'much', 'is', '?'})
        romans = [translator.foreign_to_roman(token) for token in filtered_inputs]

        if not is_roman(''.join(romans)):
            print("Invalid Roman numeral. See https://en.wikipedia.org/wiki/Roman_numerals")
            return

        all_foreign_numbers = translator.extract_all_foreign_numbers(filtered_inputs)
        numeric_value = translator.calc_foreign_numbers(all_foreign_numbers)
        print(f"{' '.join(all_foreign_numbers)} is {numeric_value}")

    except KeyError as e:
        print(f"Unknown foreign number: {e}")
        return
    except ForeignNumberException as e:
        print(f"Unknown foreign number: {e}")
        return


def is_product_question(inputs: list[str]) -> bool:
    """
    Checks if the input is a product question by verifying that it starts with "how many coins is" and ends with a question mark.
    For example, "how many coins is unu kvin Silver ?".
    :param inputs: Input list of strings.
    :return: True if the input is a product question, False otherwise.
    """
    return (
            len(inputs) >= 6  # at least 6 words are needed
            and inputs[0].lower() == "how"
            and inputs[1].lower() == "many"
            and inputs[2].lower() == "coins"
            and inputs[3].lower() == "is"
            and inputs[-1] == "?"
    )


def handle_product_question(inputs, translator):
    """
    Handles the product question by translating the foreign numbers to Roman numerals, calculating their value, and multiplying it by the known product price.
    :param inputs: Input list of strings, which should contain foreign numbers, a product name, and end with a question mark.
    :param translator: Translator instance to handle the product price logic.
    :raises ProductException: If no product name is found in the input.
    :raises ForeignNumberException: If an unknown foreign number is encountered in the input.
    """
    try:
        # Extract inputs
        product_name = extract_product_name(inputs)
        filtered_inputs = remove_keywords(inputs, {'how', 'many', 'coins', 'is', product_name, '?'})
        all_foreign_numbers = translator.extract_all_foreign_numbers(filtered_inputs)

        translated = translator.calc_foreign_numbers(all_foreign_numbers)
        product_price = translator.get_product_price(product_name)
        total = translated * product_price
        print(f"{' '.join(all_foreign_numbers)} {product_name} is {total} coins")

    except ProductException as e:
        print(e)
        return
    except ForeignNumberException as e:
        print(f"Unknown foreign number: {e}")
        return


def main():
    translator = Translator(r"./backup.pkl")
    command_map = {
        "exit": ExitCommand(),
        "print": PrintCommand(),
        "clear": ClearCommand(),
        "reset": ResetCommand(),
        "help": HelpCommand(),
        "save": SaveCommand(),
        "load": LoadCommand(),
    }

    while True:
        inputs = list(map(str, input(">> Input: ").split()))

        # edge case
        if len(inputs) == 0:
            print("Empty input. Showing help message...")
            command_map["help"].handle(inputs, translator)
            continue

        if is_command(inputs, command_map):
            handle_command(inputs, translator, command_map)
        elif is_assignment(inputs, ):
            handle_assignment(inputs, translator)
        elif is_product_price_definition(inputs):
            handle_product_price_definition(inputs, translator)
        elif is_foreign_question(inputs):
            handle_foreign_question(inputs, translator)
        elif is_product_question(inputs):
            handle_product_question(inputs, translator)
        else:
            print_error()


if __name__ == '__main__':
    main()
