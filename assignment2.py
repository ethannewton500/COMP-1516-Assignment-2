# Assignment 2 Ethan Newton

from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):
    while True:
        if re.match("[a-z0-9]{1,8}[.]txt", filename, re.I):
            valid_file_name = filename
            break
        else:
            filename = input("Please enter a new valid filename (1-8 letters or numbers ending with .txt)")

    f = open(valid_file_name, "w")
    for country, capital in countries_capitals_dictionary.items():
        f.write(f"The capital of {country} is {capital}.\n")
    f.close()


write_countries_capitals_to_file("123456789.txt")
