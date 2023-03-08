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


def save_capitals():
    # vowels
    f = open("vowel_vowel_vowel.txt", "w")
    for capital in capitals:
        if re.search("[aeiou]{3}", capital, re.I):
            f.write(f"{capital.lower()}\n")
    f.close()
    # consonants
    f = open("cons_cons_cons.txt", "w")
    for capital in capitals:
        if re.search("[^aeiou .']{3}", capital, re.I):
            f.write(f"{capital.lower()}\n")
    f.close()
    # i before e
    f = open("i_before_e.txt", "w")
    for capital in capitals:
        if re.search("i.*e", capital, re.I):
            f.write(f"{capital.lower()}\n")
    f.close()
    # start and end with a
    f = open("a_a.txt", "w")
    for capital in capitals:
        if re.search("^a.*a$", capital, re.I):
            f.write(f"{capital.lower()}\n")
    f.close()
    # end with vowel
    f = open("end_with_vowel.txt", "w")
    for capital in capitals:
        if re.search("[aeiou]$", capital, re.I):
            f.write(f"{capital.lower()}\n")
    f.close()
    # weird
    f = open("weird.txt", "w")
    for capital in capitals:
        if re.search("[' x]", capital, re.I):
            f.write(f"{capital.lower()}\n")
    f.close()
    f = open("not_start.txt", "w")
    for capital in capitals:
        if re.search("^[^a-el-ps]", capital, re.I):
            f.write(f"{capital.lower()}\n")
    f.close()


save_capitals()
