import sys

from stats import *
from reports import *
from parser import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1] 

    # retrieve file contents of filepath:
    file_contents = get_book_text(file_path)
    
    # calculate the number of words in the file:
    num_of_words = count_words(file_contents)
    
    # calculate the character frequency: 
    char_count = count_characters(file_contents)
    
    # build a sorted list from character frequencies:
    ch_sorted_list = chars_dict_to_sorted_list(char_count)

    print_report(file_path, num_of_words, ch_sorted_list)
    

main()
