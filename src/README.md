## Usage
This Project covers the solution to the Traders' Translator problem. The code is written in Python and is designed to 
handle the conversion of units, roman numerals, and prices of goods based on the input provided. Besides, the required
functionality described in TradersTranslator.md, many extra features were added to the code. For example:

- A Command Line Interface \(CLI\) was implemented to allow users to interact with the program more easily:
  - `save`: Saves current knowledge to file
  - `load`: Load backed knowledge from file
  - `clear`: Deletes all currently known \(runtime\) knowledge
  - `reset`: Resets the backed \(saved\) knowledge
  - `print <knowledge_base> | <foreign_numbers>`: Prints either all known product prices or foreign-roman translations
  - `help`: Prints this help message
  - `exit`: Exits the program

- The program can handle invalid queries appropriately.
- The program can handle all questions that are formatted as described in the TradersTranslator.md.
- Additional error handling and validation checks were implemented to ensure robustness.