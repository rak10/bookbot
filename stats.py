def get_num_words(text):
    num_words = len(text.split())
    print(f'Found {num_words} total words')
    

def char_count(text):
    lower_case_text = text.lower()
    count_dict = {}
    for char in lower_case_text:
        if not char.isalpha():
            continue
        count_dict[char]  = count_dict.get(char, 0) + 1
    return count_dict

def sort_on(items):
    return items["num"]

def sorted_dictionaries(dict):
    list_dicts = []
    for keys in dict:
        list_dicts.append({"char": keys, "num": dict[keys]})
    list_dicts.sort(reverse=True, key=sort_on)
    return list_dicts