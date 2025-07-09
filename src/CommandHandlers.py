""" Command handlers for the translator application."""

from abc import ABC, abstractmethod

from Solution1.Translator import Translator


class CommandHandlerInterface(ABC):
    """Interface for command handlers."""

    @abstractmethod
    def handle(self, inputs: list[str], translator: Translator):
        pass


class SaveCommand(CommandHandlerInterface):
    """Command to save the current knowledge to a file."""

    def handle(self, inputs, translator):
        print("Saving current knowledge to file...")
        translator.save_data()


class LoadCommand(CommandHandlerInterface):
    """Command to load the backed knowledge from a file."""

    def handle(self, inputs, translator):
        print("Loading knowledge from file...")
        translator.load_data()
        print("Product knowledge: ", translator.get_knowledge_base())
        print("Foreign numbers: ", translator.get_foreign_numbers())


class ExitCommand(CommandHandlerInterface):
    """Command to exit the program."""

    def handle(self, inputs, translator):
        print("Exiting...")
        exit()


class PrintCommand(CommandHandlerInterface):
    """Command to print the current knowledge base or foreign numbers."""

    def handle(self, inputs, translator):
        if len(inputs) < 2:
            print("Specify what to print: <knowledge_base> or <foreign_numbers>")
            return
        arg = inputs[1].lower()
        if arg == "knowledge_base":
            print(translator.get_knowledge_base())
        elif arg == "foreign_numbers":
            print(translator.get_foreign_numbers())
        else:
            print("Only <knowledge_base> or <foreign_numbers> are valid inputs")


class ClearCommand(CommandHandlerInterface):
    """Command to clear the runtime knowledge."""

    def handle(self, inputs, translator):
        translator.clear_foreign_numbers()
        translator.clear_knowledge_base()
        print("Cleared runtime knowledge...")


class ResetCommand(CommandHandlerInterface):
    """Command to reset the backed knowledge."""

    def handle(self, inputs, translator):
        translator.delete_backup()
        print("Reset backed knowledge...")


class HelpCommand(CommandHandlerInterface):
    """Command to print the help message."""

    def handle(self, inputs, translator):
        print("\nAvailable Commands:\n"
              "  save      - Saves current knowledge to file\n"
              "  load      - Load backed knowledge from file\n"
              "  clear     - Deletes all currently known (runtime) knowledge\n"
              "  reset     - Resets the backed (saved) knowledge\n"
              "  print <knowledge_base> | <foreign_numbers>\n"
              "            - Prints either all known product prices or foreign-roman translations\n"
              "  help      - Prints this help message\n"
              "  exit      - Exits the program\n"
              "\n"
              "How to use this Programm:\n"
              "This Programm translates foreign numbers and uses the roman number system as exchange numbers.\n"
              "It can also calculate the price of products in coins based on known foreign numbers.\n"
              "Each word in the input must be separated by a space.\n"
              "- First, you need to define foreign numbers and their roman number translation with the "
              "following syntax: <foreign_number> is <roman_number>.\n"
              "- You can also define product prices with the syntax: <foreign numbers seperated with spaces> is <coin_value> coins\n"
              "- You can then ask for the price of a product with the syntax: how many coins is <foreign numbers seperated with spaces> <product_name> ?\n"
              "- You can also ask for the roman value of a foreign number with the syntax: how much is <foreign numbers seperated with spaces> ?\n"
              "\n"
              "Note:\n"
              "- Invalid input (wrong syntax, unknown words, or undefined products) will result in:\n"
              "    \"I have no idea what you are talking about\"\n"
              "- The Roman numeral rules are strictly enforced. See:\n"
              "    https://en.wikipedia.org/wiki/Roman_numerals\n")
