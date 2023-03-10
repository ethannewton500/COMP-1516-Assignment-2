# Assignment 2 Ethan Newton
# UNUSED IMPORT STATEMENT ERRORS

from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):
    """
    Takes param filename and checks if it is proper filename format based of assignment2 document requirements. If it
    is not a valid filename it asks user to input a correct one. Then proceeds to write all countries and capitals to
    a txt file with that filename
    :param filename: The file name that is verified
    :return: no return
    """
    while True:
        if re.match("[a-z0-9]{1,8}[.]txt", filename, re.I):
            valid_file_name = filename
            break
        else:
            filename = input("Please enter a new valid filename (1-8 letters or numbers ending with .txt)")

    f = open(valid_file_name, "w")
    for country, capital in countries_capitals_dictionary.items():
        f.write(f"The capital of {country} is {capital}\n")
    f.close()


def save_capitals():
    """
    Creates 7 different txt files using capitals from data.py
    :return: no return
    """
    # vowels
    f = open("vowel_vowel_vowel.txt", "w")
    for capital in capitals:
        if re.search("[aeiou]{3}", capital, re.I):
            f.write(f"{capital.lower()}\n")
    f.close()
    # consonants
    f = open("cons_cons_cons.txt", "w")
    for capital in capitals:
        if re.search("[^aeiou -.']{3}", capital, re.I):
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
    # not start
    f = open("not_start.txt", "w")
    for capital in capitals:
        if re.search("^[^a-el-ps]", capital, re.I):
            f.write(f"{capital.lower()}\n")
    f.close()


def main():
    """
    main guard function
    :return: nothing
    """
    print("I should not be called")


if __name__ == '__main__':
    main()
