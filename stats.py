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

def sort_on(ch_count: tuple[str, int]) -> int:
    return ch_count[1]

def chars_dict_to_sorted_list(ch_dict: dict[str, int]) -> list[tuple[str, int]]:
    ch_list = []
    for ch in ch_dict:
        ch_list.append((ch, ch_dict[ch]))

    return sorted(ch_list, reverse=True, key=sort_on)
