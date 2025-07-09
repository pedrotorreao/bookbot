def count_words(file_contents):
    return len(file_contents.split())

def count_characters(file_contents):
    charac_dict = {}
    for ch in file_contents:
        ch_low = ch.lower()
        if ch_low in charac_dict:
            charac_dict[ch_low] += 1
        else:
            charac_dict[ch_low] = 1
   
    return charac_dict

def sort_on(d):
    return d["num"]

def sort_dict(unsorted_dict):
    sorted_list = []
    for ch in unsorted_dict:
        sorted_list.append({"char": ch, "num": unsorted_dict[ch]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
