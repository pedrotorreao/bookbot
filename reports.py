def print_report(file_path, word_count, char_sorted_list):
    print(f"""
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
""")
    for item in char_sorted_list:
        if not item[0].isalpha():
            continue
        print(f"{item[0]}: {item[1]}") 
    
    print("============= END ===============")


