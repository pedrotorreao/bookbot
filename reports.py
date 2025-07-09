def print_report(file_path, word_count, char_sorted_list):
    print(f"""
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
""")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}") 
    
    print("============= END ===============")


