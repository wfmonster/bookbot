from collections import Counter

def count_words(text):
    return len(text.split())

def count_characters(text):
    chars = Counter(text.lower())
    chars_dict = dict(chars)
    return chars_dict

def sort_characters(char_dict):
    """
    returns a sorted list of dictionaries
     {"char": "b", "num": 4868}
    """
    def sort_on(items):
        return items["num"]

    sorted_chars = []
    for char in char_dict:
        element = {"char": char, "num": char_dict[char]}
        sorted_chars.append(element)
    
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars