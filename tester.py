files = ["a_a.txt", "capitals.txt", "cons_cons_cons.txt", "end_with_vowel.txt", "i_before_e.txt", "not_start.txt",
         "vowel_vowel_vowel.txt", "weird.txt"]


def main():
    for file in files:
        filename = file
        f1 = open(f"Output TXTS/{filename}")
        file1_data = f1.read()
        f1.close()

        f2 = open(filename, "r")
        file2_data = f2.read()
        f2.close()

        if file1_data != file2_data:
            print(f"**********     error with {file}     **********")
        else:
            print(f"{file} good")


if __name__ == '__main__':
    main()
