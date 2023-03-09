# Assignment 2 Ethan Newton
# UNUSED IMPORT STATEMENT ERRORS

from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import assignment2
import re
# the assignment 2 marks document doesn't ask for import re but im including because the assignment 2 document does


def main():
    """
    simply calls the two functions created in assignment2.py
    :return: no return
    """
    assignment2.write_countries_capitals_to_file("0123456789.txt")
    assignment2.save_capitals()


if __name__ == '__main__':
    main()
