# function for counting the number of words in the text:
def count_words(str):
    words = str.split()

    return len(words)


# function for counting characters in the text:
def count_characters(str):
    charac_dict = {}
    for word in str:
        charac = word.split()
        for ch in charac:
            ch = ch.lower()
            if ch.isalpha():
                if ch in charac_dict:
                    charac_dict[ch] += 1
                else:
                    charac_dict[ch] = 1

    return charac_dict


# function for printing out a report:
def print_report(path, word_count, charac_count):
    print(f"\n--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("\n")

    for ch in charac_count:
        print(f"The {ch} character was found {charac_count[ch]} times")

    print("--- End report ---")


def main():
    # path for the text:
    file_path = "books/frankenstein.txt"

    # open file for processing:
    with open(file_path) as f:
        file_contents = f.read()

        word_count = count_words(file_contents)
        print(f"{word_count} words found")

        charac_count = count_characters(file_contents)
        print(f"letter count: {charac_count}")

        print_report(file_path, word_count, charac_count)


main()
