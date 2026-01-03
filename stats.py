

def wordcounter(text):
    allwords = text.split()
    return len(allwords)

def characterCount(text):
    text_list = text.lower()
    dictionary = {}


    for char in text_list:
        if char in dictionary:
            dictionary[char] += 1 
        
        if char not in dictionary:
            dictionary[char] = 1
    
    return dictionary


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
